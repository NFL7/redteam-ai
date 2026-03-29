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
```

---

## Configuration  

Créer un fichier `.env` à la racine du projet :  

```
OPENAI_API_KEY=your_api_key_here
```

Si la clé API n’est pas disponible ou si le quota est dépassé, une **simulation hybride** permet de générer des réponses fictives pour les agents.  

---

## Exécution  

```bash
python main.py
```

---

## Exemple de sortie  

```
--- RED TEAM SIMULATION ---

Recon: Mapping of system vulnerabilities completed.
Attack: Injection of malicious transactions successful.
AI Attack: AI model behavior altered.
Compliance: Regulatory violations detected.
Risk: High financial and reputational impact identified.
```

---

## Résultats  

La simulation permet de :  
- Identifier les vulnérabilités techniques et réglementaires  
- Tester la robustesse du système ARMS  
- Mettre en évidence des failles liées à DORA, MiCA et AI Act  
- Produire un score de risque global  

---

## Lien avec le livrable  

Les résultats détaillés (scénarios, impacts, recommandations) sont présentés dans les diapositives associées au projet.  

---

## Auteur  

Projet réalisé dans le cadre d’un atelier académique sur la sécurité et la conformité des systèmes agentiques.  
