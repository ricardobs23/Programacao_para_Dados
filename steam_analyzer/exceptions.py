class SteamDataError(Exception):
    """Exceção base para erros no módulo de análise de dados da Steam."""
    pass

class ArquivoInvalidoError(SteamDataError):
    """Lançada quando o arquivo CSV não pode ser encontrado ou lido."""
    pass

class FormatoDadoInvalidoError(SteamDataError):
    """Lançada quando há inconsistência nos tipos de dados do CSV."""
    pass