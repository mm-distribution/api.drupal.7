# FilterCRUDTestCase::verifyTextFormat()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 87–120 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L87-L120)
- **Class:** [FilterCRUDTestCase](../FilterCRUDTestCase.md)
- **Module/theme:** filter

## Signature

```php
function verifyTextFormat($format)
```

## Documentation

```text
Verifies that a text format is properly stored.
```

## Code

```php
  function verifyTextFormat($format) {
    $t_args = array('%format' => $format->name);
    // Verify text format database record.
    $db_format = db_select('filter_format', 'ff')
      ->fields('ff')
      ->condition('format', $format->format)
      ->execute()
      ->fetchObject();
    $this->assertEqual($db_format->format, $format->format, format_string('Database: Proper format id for text format %format.', $t_args));
    $this->assertEqual($db_format->name, $format->name, format_string('Database: Proper title for text format %format.', $t_args));
    $this->assertEqual($db_format->cache, $format->cache, format_string('Database: Proper cache indicator for text format %format.', $t_args));
    $this->assertEqual($db_format->weight, $format->weight, format_string('Database: Proper weight for text format %format.', $t_args));

    // Verify filter_format_load().
    $filter_format = filter_format_load($format->format);
    $this->assertEqual($filter_format->format, $format->format, format_string('filter_format_load: Proper format id for text format %format.', $t_args));
    $this->assertEqual($filter_format->name, $format->name, format_string('filter_format_load: Proper title for text format %format.', $t_args));
    $this->assertEqual($filter_format->cache, $format->cache, format_string('filter_format_load: Proper cache indicator for text format %format.', $t_args));
    $this->assertEqual($filter_format->weight, $format->weight, format_string('filter_format_load: Proper weight for text format %format.', $t_args));

    // Verify the 'cache' text format property according to enabled filters.
    $filter_info = filter_get_filters();
    $filters = filter_list_format($filter_format->format);
    $cacheable = TRUE;
    foreach ($filters as $name => $filter) {
      // If this filter is not cacheable, update $cacheable accordingly, so we
      // can verify $format->cache after iterating over all filters.
      if ($filter->status && isset($filter_info[$name]['cache']) && !$filter_info[$name]['cache']) {
        $cacheable = FALSE;
        break;
      }
    }
    $this->assertEqual($filter_format->cache, $cacheable, 'Text format contains proper cache property.');
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
