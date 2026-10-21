# UpdateTestHelper::refreshUpdateStatus()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 39–47 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L39-L47)
- **Class:** [UpdateTestHelper](../UpdateTestHelper.md)
- **Module/theme:** update

## Signature

```php
protected function refreshUpdateStatus($xml_map, $url = 'update-test')
```

## Documentation

```text
Refreshes the update status based on the desired available update scenario.

@param $xml_map
  Array that maps project names to availability scenarios to fetch. The key
  '#all' is used if a project-specific mapping is not defined.
@param $url
  (optional) A string containing the URL to fetch update data from.
  Defaults to 'update-test'.

@see update_test_mock_page()
```

## Code

```php
  protected function refreshUpdateStatus($xml_map, $url = 'update-test') {
    // Tell the Update Manager module to fetch from the URL provided by
    // update_test module.
    variable_set('update_fetch_url', url($url, array('absolute' => TRUE)));
    // Save the map for update_test_mock_page() to use.
    variable_set('update_test_xml_map', $xml_map);
    // Manually check the update status.
    $this->drupalGet('admin/reports/updates/check');
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
