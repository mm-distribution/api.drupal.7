# FilterCRUDTestCase::verifyFilters()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 125–169 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L125-L169)
- **Class:** [FilterCRUDTestCase](../FilterCRUDTestCase.md)
- **Module/theme:** filter

## Signature

```php
function verifyFilters($format)
```

## Documentation

```text
Verifies that filters are properly stored for a text format.
```

## Code

```php
  function verifyFilters($format) {
    // Verify filter database records.
    $filters = db_query("SELECT * FROM {filter} WHERE format = :format", array(':format' => $format->format))->fetchAllAssoc('name');
    $format_filters = $format->filters;
    foreach ($filters as $name => $filter) {
      $t_args = array('%format' => $format->name, '%filter' => $name);

      // Verify that filter status is properly stored.
      $this->assertEqual($filter->status, $format_filters[$name]['status'], format_string('Database: Proper status for %filter in text format %format.', $t_args));

      // Verify that filter settings were properly stored.
      $this->assertEqual(unserialize($filter->settings), isset($format_filters[$name]['settings']) ? $format_filters[$name]['settings'] : array(), format_string('Database: Proper filter settings for %filter in text format %format.', $t_args));

      // Verify that each filter has a module name assigned.
      $this->assertTrue(!empty($filter->module), format_string('Database: Proper module name for %filter in text format %format.', $t_args));

      // Remove the filter from the copy of saved $format to check whether all
      // filters have been processed later.
      unset($format_filters[$name]);
    }
    // Verify that all filters have been processed.
    $this->assertTrue(empty($format_filters), 'Database contains values for all filters in the saved format.');

    // Verify filter_list_format().
    $filters = filter_list_format($format->format);
    $format_filters = $format->filters;
    foreach ($filters as $name => $filter) {
      $t_args = array('%format' => $format->name, '%filter' => $name);

      // Verify that filter status is properly stored.
      $this->assertEqual($filter->status, $format_filters[$name]['status'], format_string('filter_list_format: Proper status for %filter in text format %format.', $t_args));

      // Verify that filter settings were properly stored.
      $this->assertEqual($filter->settings, isset($format_filters[$name]['settings']) ? $format_filters[$name]['settings'] : array(), format_string('filter_list_format: Proper filter settings for %filter in text format %format.', $t_args));

      // Verify that each filter has a module name assigned.
      $this->assertTrue(!empty($filter->module), format_string('filter_list_format: Proper module name for %filter in text format %format.', $t_args));

      // Remove the filter from the copy of saved $format to check whether all
      // filters have been processed later.
      unset($format_filters[$name]);
    }
    // Verify that all filters have been processed.
    $this->assertTrue(empty($format_filters), 'filter_list_format: Loaded filters contain values for all filters in the saved format.');
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
