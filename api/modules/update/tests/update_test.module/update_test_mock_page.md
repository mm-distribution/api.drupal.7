# update_test_mock_page()

- **Type:** Function
- **File:** [`modules/update/tests/update_test.module`](_file.md), lines 103–122 · [local source](../../../../../source/modules/update/tests/update_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/tests/update_test.module#L103-L122)
- **Module/theme:** aaa_update_test

## Signature

```php
function update_test_mock_page($project_name)
```

## Documentation

```text
Page callback: Prints mock XML for the Update Manager module.

The specific XML file to print depends on two things: the project we're
trying to fetch data for, and the desired "availability scenario" for that
project which we're trying to test. Before attempting to fetch this data (by
checking for updates on the available updates report), callers need to define
the 'update_test_xml_map' variable as an array, keyed by project name,
indicating which availability scenario to use for that project.

@param $project_name
  The project short name the update manager is trying to fetch data for (the
  fetch URLs are of the form: [base_url]/[project_name]/[core_version]).

@see update_test_menu()
```

## Code

```php
function update_test_mock_page($project_name) {
  $xml_map = variable_get('update_test_xml_map', FALSE);
  if (isset($xml_map[$project_name])) {
    $availability_scenario = $xml_map[$project_name];
  }
  elseif (isset($xml_map['#all'])) {
    $availability_scenario = $xml_map['#all'];
  }
  else {
    // The test didn't specify (for example, the webroot has other modules and
    // themes installed but they're disabled by the version of the site
    // running the test. So, we default to a file we know won't exist, so at
    // least we'll get an empty page from readfile instead of a bunch of
    // Drupal page output.
    $availability_scenario = '#broken#';
  }

  $path = drupal_get_path('module', 'update_test');
  readfile("$path/$project_name.$availability_scenario.xml");
}
```

---
_Drupal 7.103 · [modules/update/tests/update_test.module](https://github.com/drupal/drupal/blob/7.103/modules/update/tests/update_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
