# Red Team Agentic Simulation – ARMS Security Testing  

## Description  
Ce projet simule une **Red Team agentique** composée de plusieurs agents IA autonomes afin de tester la sécurité, la conformité et les risques d’un système financier cible.  

Il s’inscrit dans le cadre de l’évaluation du système **ARMS (Agentic Risk Monitoring System)** dans un environnement bancaire, en lien avec les réglementations :  
- DORA (Digital Operational Resilience Act)  
- MiCA (Markets in Crypto-Assets)  
- AI Act (régulation des systèmes d’intelligence artificielle)  

L’objectif est de simuler des attaques réalistes afin d’identifier les vulnérabilités techniques et réglementaires, puis d’en évaluer l’impact.  

---

## Agents  

| Agent | Rôle principal | Description |
|------|--------------|------------|
| Recon | Cartographie | Analyse le système et identifie les dépendances et vecteurs d’attaque |
| Attack | Simulation d’attaque | Injecte des attaques (transactions, API, etc.) |
| AI Attack | Attaque IA | Manipule les données ou les décisions du modèle |
| Compliance | Conformité | Détecte les violations RGPD / AI Act / DORA / MiCA |
| Risk | Impact & scoring | Évalue les pertes financières et le risque global |

---

## Fonctionnement  

Les agents interagissent de manière séquentielle :  

Recon → Attack → AI Attack → Compliance → Risk  

- Recon identifie les surfaces d’attaque  
- Attack exécute des attaques simulées  
- AI Attack cible le modèle d’IA  
- Compliance détecte les violations réglementaires  
- Risk mesure les impacts et produit un score  

---

## Scénarios simulés  

- **Attaque cyber conventionnelle**  
  Exemple : manipulation de transactions via API  

- **Attaque IA / data**  
  Exemple : data poisoning, biais dans la détection de fraude  

---

## Installation  

```bash
git clone https://github.com/NFL7/redteam-ai.git
cd redteam-ai
pip install -r requirements.txt
