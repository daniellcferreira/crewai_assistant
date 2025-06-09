from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from dotenv import load_dotenv
from crewai import Agent, Task, Crew

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa a ferramenta para obter notícias financeiras do Yahoo Finance
yahoo_finance_news_tool = YahooFinanceNewsTool()

# Define o agente Analista Financeiro
financial_analyst = Agent(
  role='Financial Analyst',
  goal='Analisar notícias financeiras atuais para identificar tendências de mercado e oportunidades de investimento',
  backstory=(
    "Você é um analista financeiro experiente, especialista em interpretar dados "
    "de mercado e notícias para prever tendências e aconselhar estratégias de investimento."
  ),
  verbose=True,             # Mostra logs detalhados para acompanhamento
  allow_delegation=False,   # Não permite delegação de tarefas para outros agentes
  tools=[yahoo_finance_news_tool]
)

# Define o agente Especialista em Comunicação Corporativa
communications_specialist = Agent(
  role='Corporate Communications Specialist',
  goal='Comunicar insights financeiros e tendências de mercado para os stakeholders da empresa',
  backstory=(
    "Como especialista em comunicação corporativa, você transforma dados financeiros "
    "complexos em mensagens claras e objetivas para o público interno e externo."
  ),
  verbose=True,
  allow_delegation=True,  # Permite delegação se necessário
  # (opcional) llm=another_llm
)

# Cria as tarefas a serem realizadas pelos agentes
task1 = Task(
  description=(
    "Revise as últimas notícias financeiras utilizando a ferramenta Yahoo Finance News. "
    "Identifique as principais tendências do mercado e oportunidades de investimento "
    "relevantes para o portfólio da empresa."
  ),
  agent=financial_analyst
)

task2 = Task(
  description=(
    "Com base no relatório do analista financeiro, prepare um comunicado para a imprensa. "
    "O comunicado deve destacar as tendências de mercado e oportunidades identificadas, "
    "adaptado para os stakeholders e o público geral."
  ),
  agent=communications_specialist
)

# Cria o time (crew) com os agentes e suas tarefas, executando em sequência
crew = Crew(
  agents=[financial_analyst, communications_specialist],
  tasks=[task1, task2],
  verbose=2  # Log detalhado da execução da crew
)

# Inicia a execução das tarefas da crew
result = crew.kickoff()

# Exibe o resultado final no console
print("######################")
print(result)
