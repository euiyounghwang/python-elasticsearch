
### Elasticsearch Curator

Elasticsearch Curator helps you curate, or manage, your Elasticsearch indices and snapshots by:
- Obtaining the full list of indices (or snapshots) from the cluster, as the actionable list
- Iterate through a list of user-defined filters to progressively remove indices (or snapshots) from this actionable list as needed.
- Perform various actions on the items which remain in the actionable list.
- Installation : Curator is breaking into version dependent releases. Curator 6.x will work with Elasticsearch 6.x, Curator 7.x will work with Elasticsearch 7.x, and when it is released, Curator 8.x will work with Elasticsearch 8.x.
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


### Run Curator
```bash
(.venv) ➜  python-elasticsearch git:(master) ✗ curator --config ./Curator/curator-config.yml --dry-run ./Curator/delete-indices.yml
2024-01-24 14:53:18,271 INFO      Preparing Action ID: 1, "delete_indices"
2024-01-24 14:53:18,271 INFO      Creating client object and testing connection
2024-01-24 14:53:18,271 INFO      Creating client object and testing connection
2024-01-24 14:53:18,300 INFO      GET http://localhost:9209/ [status:200 duration:0.028s]
2024-01-24 14:53:18,308 INFO      GET http://localhost:9209/_nodes/_local [status:200 duration:0.008s]
2024-01-24 14:53:18,331 INFO      GET http://localhost:9209/_cluster/state/master_node [status:200 duration:0.023s]
2024-01-24 14:53:18,332 INFO      Trying Action ID: 1, "delete_indices": No description given
2024-01-24 14:53:18,339 INFO      GET http://localhost:9209/*/_settings?expand_wildcards=open,closed [status:200 duration:0.007s]
2024-01-24 14:53:18,341 INFO      Skipping action "delete_indices" due to empty list: <class 'curator.exceptions.NoIndices'>
2024-01-24 14:53:18,341 INFO      Action ID: 1, "delete_indices" completed.
2024-01-24 14:53:18,341 INFO      All actions completed.
```


### Configure Curator Cronjob
```bash
sudo */15 * * * * curator --config /Users/euiyoung.hwang/ES/Python_Workspace/python-elasticsearch/Curator/curator-config.yml /Users/euiyoung.hwang/ES/Python_Workspace/python-elasticsearch/Curator/delete-indices.yml
```