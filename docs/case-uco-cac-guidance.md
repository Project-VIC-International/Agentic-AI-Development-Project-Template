# CASE, UCO, and CAC Ontology Guidance

Project VIC encourages interoperability across crimes against children mission tools. CASE, UCO, and the CAC Ontology help teams reuse common concepts instead of inventing new names and structures for the same investigative ideas.

## Default Guidance

Use CASE/UCO/CAC namespaces, classes, properties, and relationships as much as practical, even when your application stores data in:

- SQLite.
- PostgreSQL.
- JSON.
- CSV.
- Document databases.
- Graph databases.
- Search indexes.
- Application-specific objects.

You do not need every project to be a full ontology or graph application. Reusing ontology concepts still helps reduce future data normalization and improves interoperability across tools.

## When Ontology-First Design Helps

Ontology-first design may be especially useful when your project needs:

- Graph path finding across entities and relationships.
- Graph inferencing for finding complex or hidden relationships.
- Complex questions across mixed data sources.
- Concept resolution through subclassing.
- Interoperable exports for other investigative tools.
- Shared language across agencies, tools, and workflows.

## When to Keep It Lightweight

Keep the ontology use lightweight when:

- The project is a small workflow helper.
- The data model is still uncertain.
- The first milestone only needs a prototype.
- Full RDF/JSON-LD serialization would slow down early learning.

Even then, name fields and relationships with CASE/UCO/CAC concepts where they fit.

## Prompt for the Agent

```text
Review this project idea and identify which CASE, UCO, and CAC Ontology concepts may apply. Recommend where to reuse ontology namespaces, classes, properties, and relationships without forcing a graph database or RDF serialization unless it clearly helps the problem.
```

## References

- Cyber Domain Ontology: <https://cyberdomainontology.org/>
- CASE Ontology: <https://caseontology.org/>
- UCO Ontology: <https://unifiedcyberontology.org/>
- CAC Ontology: <https://site.cacontology.projectvic.org/>
- ECOSYSTEM: <https://github.com/vulnmaster/CASE-UCO-SDK/blob/main/docs/ECOSYSTEM.md>
- Mapping Guide <https://github.com/vulnmaster/CASE-UCO-SDK/blob/main/docs/MAPPING_GUIDE.md>
- Performance Guide: <https://github.com/vulnmaster/CASE-UCO-SDK/blob/main/docs/PERFORMANCE_GUIDE.md>
- Recipes accessible via CASE/UCO SDK's MCP server: <https://github.com/vulnmaster/CASE-UCO-SDK/tree/main/docs/recipes>

## See Also

- `.cursor/rules/ontology-alignment.mdc` for the binding agent rule.
- `examples/synthetic-data/sample-case-uco-cac.jsonc` for a commented teaching example.
- `docs/synthetic-test-data.md` for safe test data guidance.