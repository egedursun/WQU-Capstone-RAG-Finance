
####################################################################################################
#######################################   TOOL DESCRIPTIONS ########################################

TOOL_DESC_FUNDAMENTAL_DATA = """

    Function Parameters / Inputs / Arguments: 
        - query : The user's query, which will be used to retrieve the fundamental data.
        
    *** Nothing else is needed to send as an argument to this function. ***
    **********************************************************************

    Get fundamental data for a given symbol. This function will understand the user's query and
    return the fundamental data for the given symbol. The fundamental data response includes the following relevant
    information. Please note that the fundamental data is retrieved from SEC filings:
    
        - acceptance_datetime : The datetime (EST timezone) the filing was accepted by EDGAR in YYYYMMDDHHMMSS format.
        - cik : The CIK number for the company.
        - company_name : The company name.
        - end_date : The end date of the period that these financials cover in YYYYMMDD format.
        - filing_date : The date that the SEC filing which these financials were derived from was made available. 
                        Note that this is not necessarily the date when this information became public, 
                        as some companies may publish a press release before filing with the SEC.

        - financials(object)
        - balance_sheet(object) : The keys in this object can be any of the fields listed in the Balance Sheet section 
        of the financials API glossary of terms.
        - cash_flow_statement(object) : The keys in this object can be any of the fields listed in the Cash Flow 
        Statement section of the financials API glossary of terms. See the attributes of the objects within 
        balance_sheet for more details.
        - comprehensive_income(object) : The keys in this object can be any of the fields listed in the 
        Comprehensive Income section of the financials API glossary of terms. See the attributes of the
         objects within balance_sheet for more details.
        - income_statement(object) : The keys in this object can be any of the fields listed in the Income 
        Statement section of the financials API glossary of terms. See the attributes of the objects within 
        balance_sheet for more details.
        - fiscal_period : Fiscal period of the report according to the company (Q1, Q2, Q3, Q4, or FY).
        - fiscal_year :  Fiscal year of the report according to the company.
        
    You can directly interpret the results returned from this function to provide
    an answer to the user's query, by analyzing it according to the user's question.
"""

TOOL_DESC_TECHNICAL_DATA = """
    Function Parameters / Inputs / Arguments: 
        - query : The user's query, which will be used to retrieve the fundamental data.
        
    *** Nothing else is needed to send as an argument to this function. ***
    **********************************************************************
    
    Get technical data for a given symbol. This function will understand the user's query and
    return the technical data for the given symbol. The technical data response includes the following relevant
    information:
    
    c : The close price for the symbol in the given time period.  
    h : The highest price for the symbol in the given time period.
    l : The lowest price for the symbol in the given time period.
    n : The number of transactions in the aggregate window.
    o : The open price for the symbol in the given time period.
    otc : Whether or not this aggregate is for an OTC ticker. This field will be left off if false.
    t : The Unix Msec timestamp for the start of the aggregate window.
    v : The trading volume of the symbol in the given time period.
    vw : The volume weighted average price.
    
    You can directly interpret the results returned from this function to provide
    an answer to the user's query, by analyzing it according to the user's question.
"""

TOOL_DESC_TECHNICAL_INDICATORS = """
    Function Parameters / Inputs / Arguments: 
        - query : The user's query, which will be used to retrieve the fundamental data.
        
    *** Nothing else is needed to send as an argument to this function. ***
    **********************************************************************
    
    Get technical indicators for a given symbol. This function will understand the user's query and
    return the technical indicators for the given symbol. The technical indicators response includes the following
    relevant information:
    
    - SMA: Simple Moving Average
    - EMA: Exponential Moving Average
    - MACD: Moving Average Convergence Divergence
    - RSI: Relative Strength Index
    
    These technical indicators are calculated in the function you will call, and you don't need to
    calculate them yourself. You can directly interpret the results returned from this function to provide
    an answer to the user's query, by analyzing it according to the user's question.
"""

TOOL_DESC_TICKER_NEWS = """
    Function Parameters / Inputs / Arguments: 
        - query : The user's query, which will be used to retrieve the fundamental data.
        
    *** Nothing else is needed to send as an argument to this function. ***
    **********************************************************************
    
    Get ticker news for a given symbol. This function will understand the user's query and
    return the ticker news for the given symbol. The ticker news response includes the following relevant
    information:
    
    - article_url : A link to the news article.
    - author : The article's author.
    - description : A description of the article.
    - keywordsarray : The keywords associated with the article (which will vary depending on the publishing source).
    - published_utc : The date the article was published on.
    - publisher(object)
    - title : The title of the article.
    
    You can directly interpret the results returned from this function to provide
    an answer to the user's query, by analyzing it according to the user's question.
"""

TOOL_DESC_DIVIDENDS = """
    Function Parameters / Inputs / Arguments: 
        - query : The user's query, which will be used to retrieve the fundamental data.
        
    *** Nothing else is needed to send as an argument to this function. ***
    **********************************************************************
    
    Get dividends for a given symbol. This function will understand the user's query and
    return the dividends for the given symbol. The dividends response includes the following relevant
    information:
    
    - cash_amount : The cash amount of the dividend per share owned.  
    - currency : The currency in which the dividend is paid. 
    - declaration_date : The date that the dividend was announced. 
    - dividend_type : The type of dividend. Dividends that have been paid and/or are expected to be paid on consistent 
                    schedules are denoted as CD. Special Cash dividends that have been paid that are infrequent or 
                    unusual, and/or can not be expected to occur in the future are denoted as SC. Long-Term and 
                    Short-Term capital gain distributions are denoted as LT and ST, respectively.   
    - ex_dividend_date : The date that the stock first trades without the dividend, determined by the exchange.
    - frequency : The number of times per year the dividend is paid out. Possible values are 0 (one-time), 
    1 (annually), 2 (bi-annually), 4 (quarterly), and 12 (monthly). 
    - pay_date : The date that the dividend is paid out.
    - record_date : The date that the stock must be held to receive the dividend, set by the company.
    
    You can directly interpret the results returned from this function to provide
    an answer to the user's query, by analyzing it according to the user's question.
"""


##########################################################################################################
##################################### RUN CODE DESCRIPTIONS ##############################################


TOOL_DESC_RUN_CODE = """
    Function Parameters / Inputs / Arguments:
        - query : The user's query, which will be used to create a Python code snippet.
        
    *** Nothing else is needed to send as an argument to this function. ***
    
    **********************************************************************
    
    Run code for a given query. This function will understand the user's query and
    return the result of the Python code snippet created from the user's query. The code snippet is ran 
    through the Python interpreter, and the result is returned. Then, the agent is able to use the result
    to answer the user's query.
    
    You can directly interpret the results returned from this function to provide
    an answer to the user's query, by analyzing it according to the user's question.
    
    Details:
    
    - You can use Numpy and Pandas libraries in your code snippet. You need to import them in your code snippet.
      For example, libraries like: arch, numpy, pandas, matplotlib, etc.
    - The things you can use the code is primarily for financial engineering applications.
      - For example, ARCH, GARCH, and other financial engineering calculations, as well as Monte Carlo simulations.
"""


##########################################################################################################
##########################################################################################################



