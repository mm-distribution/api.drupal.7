# _update_get_fetch_url_base()

- **Type:** Function
- **File:** [`modules/update/update.fetch.inc`](_file.md), lines 334–336 · [local source](../../../../source/modules/update/update.fetch.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.fetch.inc#L334-L336)
- **Module/theme:** update

## Signature

```php
function _update_get_fetch_url_base($project)
```

## Documentation

```text
Returns the base of the URL to fetch available update data for a project.

@param $project
  The array of project information from update_get_projects().

@return
  The base of the URL used for fetching available update data. This does
  not include the path elements to specify a particular project, version,
  site_key, etc.

@see _update_build_fetch_url()
```

## Code

```php
function _update_get_fetch_url_base($project) {
  return isset($project['info']['project status url']) ? $project['info']['project status url'] : variable_get('update_fetch_url', UPDATE_DEFAULT_URL);
}
```

---
_Drupal 7.103 · [modules/update/update.fetch.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.fetch.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
