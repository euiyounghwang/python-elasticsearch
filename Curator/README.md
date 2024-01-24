
### Elasticsearch Curator

Elasticsearch Curator helps you curate, or manage, your Elasticsearch indices and snapshots by:
- Obtaining the full list of indices (or snapshots) from the cluster, as the actionable list
- Iterate through a list of user-defined filters to progressively remove indices (or snapshots) from this actionable list as needed.
- Perform various actions on the items which remain in the actionable list.
- Installation
```bash
(.venv) ➜  python-elasticsearch git:(master) ✗ poetry add elasticsearch-curator       
Using version ^8.0.8 for elasticsearch-curator

Updating dependencies
Resolving dependencies... (0.8s)

Package operations: 6 installs, 0 updates, 0 removals

  • Installing elastic-transport (8.12.0)
  • Installing elasticsearch8 (8.8.2)
  • Installing voluptuous (0.14.1)
  • Installing ecs-logging (2.0.2)
  • Installing es-client (8.8.2.post1)
  • Installing elasticsearch-curator (8.0.8)

Writing lock file
```