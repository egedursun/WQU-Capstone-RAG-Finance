import datetime

import dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import ChatMessage
from langchain.tools import tool
import streamlit as st

from tools.PolygonAPIClient import PolygonClient


dotenv.load_dotenv()
config = dotenv.dotenv_values()


@tool("get_fundamental_data", return_direct=True)
def get_fundamental_data(query):
    """
    Get fundamental data for a given symbol.
    """

    current_date_string = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    llm = ChatOpenAI(openai_api_key=config["OPENAI_API_KEY"],
                     streaming=False,
                     model_name="gpt-4",
                     temperature="0.5",
                     max_tokens="2048")

    with st.spinner("Internal Agent [Fundamental Data Agent] is transforming your request..."):
        json_request_url = llm(
            [ChatMessage(role="user", content=f"""
                            The user asked the following query to another GPT agent:
    
                            - {query}
                            
                            - Here is the current date in case you might need it: {current_date_string}
    
                            ---
                            
                            "NEVER TRY TO RETRIEVE THE DATA MORE THAN TWICE"
                            "ONLY ANSWER IN PLAIN TEXT"
    
                            Based on the user's query, you need to query an API to provide the required fundamental data to the
                            other agent. The agent might need this information to make a decision about a stock, or something
                            else. Still, your only task is to create the API request parameters for the other agent.
                            Your task is to generate the API request parameters with a "space character" between each parameter.
    
                            The API request parameters are:
                            - ticker_symbol : The symbol of the ticker in the financial / stocks market (e.g. AAPL)
                            - timeframe : The period of time to get the fundamental data for, the options are:
                                    - annual, quarterly, ttm
                            - limit : The maximum number of fundamental data to get. (e.g. 1) 
                            Please note that the maximum limit is 1, and further value will 
                            still return 1 fundamental data.
    
                            ---
    
                            Here is an example of what you must return:
    
                            AAPL annual 1
    
                            ---
                            
                            - IMPORTANT NOTE:
        
                            -- DO NOT ''PUT YOUR ANSWER IN MARKDOWN FORMAT''. YOU SHOULD RETURN YOUR ANSWER IN ''PLAIN TEXT''.
                            -- DO NOT PUT 'FORMULAS', 'MATH EQUATIONS', 'MATH SYMBOLS', 'MATH NOTATIONS', 'MATH FORMULAS', ETC.
                            -- DO NOT PUT 'LATEX FORMAT'. ALWAYS RETURN YOUR ANSWER IN 'PLAIN TEXT'.
                        """)]
        )
    st.success("Internal Agent [Fundamental Data Agent] has transformed your request successfully!")

    with st.spinner("Internal Agent [Fundamental Data Agent] is querying the Polygon API..."):
        parameters = json_request_url.content.split(" ")
        ticker_symbol = parameters[0].strip()
        timeframe = parameters[1].strip()
        max_limit = parameters[2].strip()

        p = PolygonClient()
        fundamental_data = p.get_fundamental(
            ticker_symbol=ticker_symbol,
            timeframe=timeframe,
            max_limit=max_limit
        )
    st.success("Internal Agent [Fundamental Data Agent] has queried the Polygon API successfully!")

    with st.expander("Reference Data [Fundamental Data API]", expanded=False):
        st.warning(str("\n\n" + str(fundamental_data) + "\n\n"))
        st.warning(str("Source: \n\n [1]  " + config["POLYGON_API_URL"] + "\n\n"))

    cutoff = -1
    if len(str(fundamental_data)) > 4_000:
        cutoff = 4_000
    return str(fundamental_data)[0:cutoff]


if __name__ == "__main__":
    print(get_fundamental_data("What is the fundamental data of AAPL of last year?"))
