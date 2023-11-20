from langchain.tools import Tool

from config import TOOL_DESC_FUNDAMENTAL_DATA, TOOL_DESC_TECHNICAL_DATA, TOOL_DESC_TECHNICAL_INDICATORS, \
    TOOL_DESC_TICKER_EVENTS, TOOL_DESC_TICKER_NEWS, TOOL_DESC_DIVIDENDS, FUNC_DESC_GET_ARCH_CALCULATIONS, \
    FUNC_DESC_GET_GARCH_CALCULATIONS, FUNC_DESC_GET_DESCRIPTIVE_STATISTICS
from functions.container.arch import get_arch_calculations
from functions.container.descriptive_statistics import get_descriptive_statistics
from functions.container.garch import get_garch_calculations
from knowledge.vector.WeaviateClient import WeaviateClient
from tools.container.dividends import get_dividends
from tools.container.fundamental_data import get_fundamental_data
from tools.container.technical_data import get_technical_data
from tools.container.technical_indicators import get_technical_indicators
from tools.container.ticker_events import get_ticker_events
from tools.container.ticker_news import get_ticker_news


class ToolManager:

    def __init__(self, llm=None, vectorstore=WeaviateClient().connection):
        self.tools = [

            ####################################################################################################
            # API TOOLS
            ####################################################################################################
            Tool("get_fundamental_data", get_fundamental_data, TOOL_DESC_FUNDAMENTAL_DATA),
            Tool("get_technical_data", get_technical_data, TOOL_DESC_TECHNICAL_DATA),
            Tool("get_technical_indicators", get_technical_indicators, TOOL_DESC_TECHNICAL_INDICATORS),
            Tool("get_ticker_events", get_ticker_events, TOOL_DESC_TICKER_EVENTS),
            Tool("get_ticker_news", get_ticker_news, TOOL_DESC_TICKER_NEWS),
            Tool("get_dividends", get_dividends, TOOL_DESC_DIVIDENDS),

            ####################################################################################################
            # FUNCTION TOOLS
            ####################################################################################################
            Tool("get_arch_calculations", get_arch_calculations, FUNC_DESC_GET_ARCH_CALCULATIONS),
            Tool("get_garch_calculations", get_garch_calculations, FUNC_DESC_GET_GARCH_CALCULATIONS),
            Tool("get_descriptive_statistics", get_descriptive_statistics, FUNC_DESC_GET_DESCRIPTIVE_STATISTICS),

        ]
        self.llm = llm
        self.vectorstore = vectorstore
        self.chat_agent = None
