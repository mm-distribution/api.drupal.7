# drupal_path_alias_whitelist_rebuild()

- **Type:** Function
- **File:** [`includes/path.inc`](_file.md), lines 368–387 · [local source](../../../source/includes/path.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/path.inc#L368-L387)

## Signature

```php
function drupal_path_alias_whitelist_rebuild($source = NULL)
```

## Documentation

```text
Rebuild the path alias white list.

@param $source
  An optional system path for which an alias is being inserted.

@return
  An array containing a white list of path aliases.
```

## Code

```php
function drupal_path_alias_whitelist_rebuild($source = NULL) {
  // When paths are inserted, only rebuild the whitelist if the system path
  // has a top level component which is not already in the whitelist.
  if (!empty($source)) {
    $whitelist = variable_get('path_alias_whitelist', NULL);
    if (isset($whitelist[strtok($source, '/')])) {
      return $whitelist;
    }
  }
  // For each alias in the database, get the top level component of the system
  // path it corresponds to. This is the portion of the path before the first
  // '/', if present, otherwise the whole path itself.
  $whitelist = array();
  $result = db_query("SELECT DISTINCT SUBSTRING_INDEX(source, '/', 1) AS path FROM {url_alias}");
  foreach ($result as $row) {
    $whitelist[$row->path] = TRUE;
  }
  variable_set('path_alias_whitelist', $whitelist);
  return $whitelist;
}
```

---
_Drupal 7.103 · [includes/path.inc](https://github.com/drupal/drupal/blob/7.103/includes/path.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
