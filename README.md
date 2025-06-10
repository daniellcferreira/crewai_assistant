# CrewAI Assistant para Análise Financeira e Recrutamento

![Python](https://img.shields.io/badge/Python-backend-blue?style=flat-square&logo=python)
![CrewAI](https://img.shields.io/badge/CrewAI-Agente%20Inteligente-6f42c1?style=flat-square)
![LangChain](https://img.shields.io/badge/LangChain-Ferramentas%20IA-ef8a17?style=flat-square)
![YahooFinance](https://img.shields.io/badge/Yahoo%20Finance%20News-Tool-430297?style=flat-square)
![SerpAPI](https://img.shields.io/badge/SerpAPI-Search%20API-blueviolet?style=flat-square)

## Descrição

Este projeto utiliza a biblioteca CrewAI para criar agentes autônomos inteligentes com papéis e tarefas específicas em dois cenários principais:  
**análise de notícias financeiras** e **busca de vagas de emprego para recrutamento**.  

Com base no paradigma de agentes, cada tarefa é realizada por um personagem virtual com objetivos bem definidos e acesso a ferramentas externas via integração com LangChain.

A execução das tarefas ocorre de forma sequencial, com comunicação implícita entre os agentes via estrutura de tarefas do CrewAI. O projeto também integra ferramentas de notícias financeiras (Yahoo Finance) e pesquisa de vagas de emprego (Google Jobs via SerpAPI).

O objetivo é demonstrar como é possível aplicar inteligência artificial generativa para automatizar análises de contexto real em ambientes corporativos.

## Funcionalidades

- Buscar as últimas notícias financeiras com base no mercado atual.
- Gerar um relatório com tendências e oportunidades de investimento.
- Criar um comunicado institucional (press release) com base na análise de mercado.
- Consultar vagas abertas em desenvolvimento de software usando Google Jobs.
- Elaborar descrições de vagas e posts atrativos para redes sociais com base nas oportunidades encontradas.
- Utilizar agentes especializados com perfis distintos para cada tarefa (ex: analista financeiro, comunicador corporativo, recrutador etc).
- Executar agentes de forma autônoma e coordenada utilizando CrewAI.
- Permitir personalização dos prompts e tarefas dos agentes para diferentes contextos.

## Tecnologias Utilizadas

- **Python 3.10+**: linguagem base do projeto.
- **CrewAI**: biblioteca de orquestração de agentes inteligentes autônomos com tarefas e fluxos.
- **LangChain Community Tools**: ferramentas especializadas para integração com fontes externas.
- **Yahoo Finance News Tool**: ferramenta de coleta de notícias financeiras em tempo real.
- **Google Jobs API Wrapper**: integração com buscas de vagas no Google Jobs via SerpAPI.
- **SerpAPI**: API para automatizar pesquisas no Google e outros serviços.
- **Python Dotenv**: carregamento automático de variáveis de ambiente via `.env`.

## Requisitos

- Conta gratuita na [SerpAPI](https://serpapi.com) para realizar buscas no Google Jobs.
- Python instalado na máquina.
- Ambiente virtual ativo (`venv`).
- Arquivo `.env` com a variável `SERPAPI_API_KEY` configurada para o módulo de recrutamento funcionar.

---

Este projeto é ideal para fins educacionais e experimentação com arquiteturas baseadas em agentes inteligentes.  
Você pode expandir ou adaptar para uso interno em empresas com necessidades específicas de análise de dados e RH.
