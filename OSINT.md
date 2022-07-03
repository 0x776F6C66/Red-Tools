# OSINT

- whois lookups - find info about domains
- netcraft - whois except better and much more info
- google hacking - google dorking e.g
	~~~
	• ext:pdf - search for "pdf" extension
	• intext:"pass" - Searches for "pass" in the content of the page
	• allintext - Similar to intext, but searches for all terms to be present in the text.
	• "A" OR "B" - show results that have Either A or B 
	• "wolf" - search for the specific word
	• before:date / after:date - give results after the particular/ before date specified
	• site:"domain name" - only info coming from the specific domain
	• filetype:xml - search for files of type "xml"
	• filename:users - search for files having the name "users" 
	• inurl: "password" - search for "password" in the url
	• intitle:"index of" - results have "index of" in their html titles
	• allintitle - similar to intitle but looks for all the specified terms in the title
	• link:www.google.com - list webpages that have links pointing to google
	• info:www.google.com - show information about google
	~~~
	**exploits can be found at exploit db**
	
- website recon - e.g Frameworks like recon-ng
- gitrob & gitleaks - find sensitive info in git repositories
- shodan -- find devices connected to the internet e.g
	~~~
	• in search bar: hostname:"domain name" -- find open ports and devices of the specified hostname
	~~~
	
- Email harvesing
	~~~
	• theharvester
	~~~
	**emails harvested could be used to check for password dumps in places like pastebin**
	
- Social Searcher - search engine for social media sites
- Twofi - scan's a user's twittes feed and generates wordlistsa(personalized) for password attacks against the user
- linkedin2username - script for generating username lists based on LinkedIn data. It requires
valid LinkedIn credentials and depends on a LinkedIn connection to individuals in the target
organization. The script will output usernames in several different formats.
- Frameworks - OSINT Framework, Maltego

## Images - reverse lookup images
- google images
- yandex
- bing images
- tin eye


---
## DNS
## DNS Records and lookups
	~~~
	• NS - Nameserver records contain the name of the authoritative servers hosting the DNS records for a domain.
	• A - contains the IP address of a hostname.
	• MX (Mail Exchange)- contain the names of the servers responsible for handling email for a domain.
	• PTR (Pointer Records) - used in reverse lookup zones and are used to find the records associated with an IP address.
	• CNAME - used to create aliases for other host/(A) records.
	• TXT (Text records)- may contain any arbitrary data, can also be used for various purposes 
	~~~
	
	## DNS Zone Transfers
	A DNS zone is used to host the DNS records for a particular domain. To hosting your domain in a DNS server, you need
	to create a DNS zone for that domain name. Each DNS record for your domain is then created inside this DNS zone.
	
	A zone transfer is basically replicating a DNS zone file from a master dns server to a slave server.
	The zone file contains a list of all the DNS names configured for a speific zone.
	~~~
	dig axfr(zone transfer) @dns-server domain
	host -l(list zone) "domain name" "dns server"
	~~~
	
	## Tools
	~~~
	• dig - dig @dns-server(optional) "domain name"/ "ip address"
	• host - host "domain name"
	• Dnsenum
	• dnsrecon
	~~~
	---
