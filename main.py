import os
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError, RateLimitError, AuthenticationError

# ----- Charger la clé depuis le fichier .env -----
load_dotenv(dotenv_path=r"C:\Users\PC\redteam-ai\.env")

api_key = os.getenv("OPENAI_API_KEY")
print("API KEY LUE :", api_key)  # juste pour vérifier
if not api_key:
    raise ValueError("La clé API n'a pas été trouvée dans .env !")

# ----- Initialiser le client OpenAI -----
client = OpenAI(api_key=api_key)

# ----- Fonction hybride pour simuler les agents si quota dépassé -----
def run_agent(prompt: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except (RateLimitError, AuthenticationError, OpenAIError):
        # Réponses simulées si problème avec l'API
        fallback = {
            "Find vulnerabilities in ARMS system": "Recon agent mapped several API vulnerabilities.",
            "Exploit API and inject fake transactions": "Attack agent injected fake transactions successfully.",
            "Manipulate fraud detection AI": "AI adversary corrupted AI decisions.",
            "Check GDPR violations": "Compliance agent detected GDPR and AI Act issues.",
            "Evaluate financial impact": "Risk agent estimated high financial and reputational impact."
        }
        return fallback.get(prompt, "No action performed.")

# ----- Simulation des 5 agents -----
print("\n--- RED TEAM SIMULATION ---\n")

print("Recon:", run_agent("Find vulnerabilities in ARMS system"))
print("Attack:", run_agent("Exploit API and inject fake transactions"))
print("AI Attack:", run_agent("Manipulate fraud detection AI"))
print("Compliance:", run_agent("Check GDPR violations"))
print("Risk:", run_agent("Evaluate financial impact"))