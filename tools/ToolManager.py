import dotenv
from langchain.agents import StructuredChatAgent, AgentExecutor
from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool

from config import TOOL_DESC_FUNDAMENTAL_DATA, TOOL_DESC_TECHNICAL_DATA, TOOL_DESC_TECHNICAL_INDICATORS, \
    TOOL_DESC_TICKER_NEWS, TOOL_DESC_DIVIDENDS, FUNC_DESC_GET_ARCH_CALCULATIONS, \
    FUNC_DESC_GET_GARCH_CALCULATIONS, FUNC_DESC_GET_DESCRIPTIVE_STATISTICS
from functions.container.arch import get_arch_calculations
from functions.container.descriptive_statistics import get_descriptive_statistics
from functions.container.garch import get_garch_calculations
from knowledge.vector.WeaviateClient import WeaviateClient
from tools.container.dividends import get_dividends
from tools.container.fundamental_data import get_fundamental_data
from tools.container.technical_data import get_technical_data
from tools.container.technical_indicators import get_technical_indicators
from tools.container.ticker_news import get_ticker_news


dotenv.load_dotenv()
config = dotenv.dotenv_values()


class ToolManager:

    def __init__(self, vectorstore=WeaviateClient().connection):
        self.tools = [

            ####################################################################################################
            # API TOOLS
            ####################################################################################################
            Tool("get_fundamental_data", get_fundamental_data, TOOL_DESC_FUNDAMENTAL_DATA),
            Tool("get_technical_data", get_technical_data, TOOL_DESC_TECHNICAL_DATA),
            Tool("get_technical_indicators", get_technical_indicators, TOOL_DESC_TECHNICAL_INDICATORS),
            Tool("get_ticker_news", get_ticker_news, TOOL_DESC_TICKER_NEWS),
            Tool("get_dividends", get_dividends, TOOL_DESC_DIVIDENDS),

            ####################################################################################################
            # FUNCTION TOOLS
            ####################################################################################################
            Tool("get_arch_calculations", get_arch_calculations, FUNC_DESC_GET_ARCH_CALCULATIONS),
            Tool("get_garch_calculations", get_garch_calculations, FUNC_DESC_GET_GARCH_CALCULATIONS),
            Tool("get_descriptive_statistics", get_descriptive_statistics, FUNC_DESC_GET_DESCRIPTIVE_STATISTICS),

        ]
        self.llm = ChatOpenAI(openai_api_key=config["OPENAI_API_KEY"],
                              streaming=True,
                              model_name="gpt-4-1106-preview",
                              temperature="0.5")
        self.vectorstore = vectorstore
        self.structured_agent = StructuredChatAgent.from_llm_and_tools(
            llm=self.llm,
            tools=self.tools)
        self.chat_agent = AgentExecutor.from_agent_and_tools(
            agent=self.structured_agent,
            tools=self.tools
        )
