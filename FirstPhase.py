from flask import Flask, render_template, request
from rdflib import Graph, Namespace
from rdflib.namespace import RDF, OWL, RDFS, XSD

app = Flask(__name__)

g = Graph()
g.parse("json-ontology.jsonld", format="json-ld")  # OWL file path and format


# Namespace definition
ns = Namespace("http://www.semanticweb.org/satilmis/ontologies/2024/10/ontologygame#")
g.bind(":", ns)
g.bind("rdf", RDF)
g.bind("owl", OWL)
g.bind("rdfs", RDFS)
g.bind("xsd", XSD)

@app.route("/", methods=["GET", "POST"])
def home():
    platforms = request.form.getlist("platform")
    genres = request.form.getlist("genre")
    difficulties = request.form.getlist("difficulty")


    sparql_query = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX : <http://www.semanticweb.org/satilmis/ontologies/2024/10/ontologygame#>

    SELECT DISTINCT ?game
    WHERE {
    """

    filters = []

    # Add platform filter
    if "any" not in platforms:
        for platform in platforms:
            filters.append(f"""
                ?game rdfs:subClassOf [
                    rdf:type owl:Restriction ;
                    owl:onProperty :hasPlatform ;
                    owl:someValuesFrom :{platform}
                ] .
            """)

    # Add genre filter
    if "any" not in genres:
        for genre in genres:
            filters.append(f"""
                ?game rdfs:subClassOf [
                    rdf:type owl:Restriction ;
                    owl:onProperty :hasGenre ;
                    owl:someValuesFrom :{genre}
                ] .
            """)

    # Add difficulty filter
    if "any" not in difficulties:
        filters.append("""
            ?game rdfs:subClassOf [
                rdf:type owl:Restriction ;
                owl:onProperty :hasDifficulty
            ] .
        """)

    # Combine filters into the query
    sparql_query += "\n".join(filters)
    sparql_query += "\n}"

    # Execute the SPARQL query
    results = g.query(sparql_query)

    # Extract results
    games = [str(row.game) for row in results]
    # Extract the local name (after '#') from each result
    games = [str(row.game).split("#")[-1] for row in results]
    return render_template("index.html", games=games)

if __name__ == "__main__":
    app.run(debug=True,port=5051)
