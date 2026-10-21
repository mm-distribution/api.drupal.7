# dblog_filters()

- **Type:** Function
- **File:** [`modules/dblog/dblog.admin.inc`](_file.md), lines 250–272 · [local source](../../../../source/modules/dblog/dblog.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.admin.inc#L250-L272)
- **Module/theme:** dblog

## Signature

```php
function dblog_filters()
```

## Documentation

```text
Creates a list of database log administration filters that can be applied.

@return array
  Associative array of filters. The top-level keys are used as the form
  element names for the filters, and the values are arrays with the following
  elements:
  - title: Title of the filter.
  - where: The filter condition.
  - options: Array of options for the select list for the filter.
```

## Code

```php
function dblog_filters() {
  $filters = array();

  foreach (_dblog_get_message_types() as $type) {
    $types[$type] = t($type);
  }

  if (!empty($types)) {
    $filters['type'] = array(
      'title' => t('Type'),
      'where' => "w.type = ?",
      'options' => $types,
    );
  }

  $filters['severity'] = array(
    'title' => t('Severity'),
    'where' => 'w.severity = ?',
    'options' => watchdog_severity_levels(),
  );

  return $filters;
}
```

---
_Drupal 7.103 · [modules/dblog/dblog.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
