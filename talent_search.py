from dotenv import load_dotenv
from langchain_community.tools.google_jobs import GoogleJobsQueryRun
from langchain_community.utilities.google_jobs import GoogleJobsAPIWrapper
from crewai import Agent, Task, Crew

# Carrega variáveis de ambientes de arquivo .env
load_dotenv()

# Inicializa a ferramenta para busca de vagas de Google Jobs
google_jobs_tool = GoogleJobsQueryRun(api_wrapper=GoogleJobsAPIWrapper())

# Define o agente especialista em recrutamento
recruitment_specialist = Agent(
  role="Recruitment Specialist",
  goal="Encontrar candidatos adequados para várias posições na empresa",
  backstory=(
    "Você é um especialista em recrutamento com experiência em identificar e atrair "
    "os melhores talentos em diversos setores e funções."
  ),
  verbose=True,           # Ativa logs detalhados
  allow_delegation=True,  # Permite delegar tarefas para outros agentes
  tools=[google_jobs_tool] 
)

# Define o agente coordenador de comunicação de RH
hr_communicator = Agent(
  role="HR Communications Coordinator",
  goal="Comunicar vagas abertas e cultura da empresa para potenciais candidatos",
  backstory=(
    "Como coordenador de comunicação de RH, você é especialista em criar descrições "
    "atraentes para vagas e promover os valores e cultura da empresa para atrair os candidatos ideias."
  ),
  verbose=True,
  allow_delegation=True
)

# Cria as tarefas para os agentes
task1 = Task(
  description=(
    "Identificar vagas atuais na área de desenvolvimento de software usando a ferramenta Google Jobs. "
    "Focar em cargos adequados para candidatos com 1 a 3 anos experiência."
  ),
  agent=recruitment_specialist
)

task2 = Task(
  description=(
    "Com base na vagas identificadas, criar descrições de cargos envolventes e uma postagem para redes socias. "
    "Enfatizar o compromisso da empresa com inovação e um ambiente de trabalho colaborativo."
  ),
  agent=hr_communicator
)

# Instancia a crew com execução sequencial das tarefas
crew = Crew(
  agents=[recruitment_specialist, hr_communicator],
  tasks=[task1, task2],
  verbose=2
)

# Inicia a execução das tarefas da crew
result = crew.kickoff()

# Exibe o resultado
print("#" * 30)
print(result)