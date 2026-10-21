# filter_update_7001()

- **Type:** Function
- **File:** [`modules/filter/filter.install`](_file.md), lines 199–217 · [local source](../../../../source/modules/filter/filter.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.install#L199-L217)
- **Module/theme:** filter
- **Topics:** [updates-6.x-to-7.x](../../../topics/updates-6.x-to-7.x.md)

## Signature

```php
function filter_update_7001()
```

## Documentation

```text
Break out "escape HTML filter" option to its own filter.
```

## Code

```php
function filter_update_7001() {
  $result = db_query("SELECT format FROM {filter_format}")->fetchCol();
  $insert = db_insert('filters')->fields(array('format', 'module', 'delta', 'weight'));

  foreach ($result as $format_id) {
    // Deprecated constants FILTER_HTML_STRIP = 1 and FILTER_HTML_ESCAPE = 2.
    if (variable_get('filter_html_' . $format_id, 1) == 2) {
      $insert->values(array(
        'format' => $format_id,
        'module' => 'filter',
        'delta' => 4,
        'weight' => 0,
      ));
    }
    variable_del('filter_html_' . $format_id);
  }

  $insert->execute();
}
```

---
_Drupal 7.103 · [modules/filter/filter.install](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.install) · Licensed GPL-2.0-or-later (see LICENSE)._
