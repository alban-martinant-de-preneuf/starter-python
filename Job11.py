import re

extensionsDomains = []

with open("domains.xml") as domainsFile:
    domains = re.findall(r"\.[a-z]{1,}[<\s]", domainsFile.read())
    for domain in domains:
        domain = domain[:-1]
        if domain not in extensionsDomains:
            extensionsDomains.append(domain)

nbExtensionsDomains = 0
for element in extensionsDomains:
    nbExtensionsDomains += 1

print("Il y a " + str(nbExtensionsDomains) + " extensions de domaine différentes.")