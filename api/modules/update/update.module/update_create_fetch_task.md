# update_create_fetch_task()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 458–461 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L458-L461)
- **Module/theme:** update

## Signature

```php
function update_create_fetch_task($project)
```

## Documentation

```text
Creates a new fetch task after loading the necessary include file.

@param $project
  Associative array of information about a project. See update_get_projects()
  for the keys used.

@see _update_create_fetch_task()
```

## Code

```php
function update_create_fetch_task($project) {
  module_load_include('inc', 'update', 'update.fetch');
  return _update_create_fetch_task($project);
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
