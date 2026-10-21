# HelpTestCase::getModuleList()

- **Type:** Method
- **File:** [`modules/help/help.test`](../_file.md), lines 98–107 · [local source](../../../../../source/modules/help/help.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/help/help.test#L98-L107)
- **Class:** [HelpTestCase](../HelpTestCase.md)
- **Module/theme:** help

## Signature

```php
protected function getModuleList()
```

## Documentation

```text
Gets the list of enabled modules that implement hook_help().

@return array
  A list of enabled modules.
```

## Code

```php
  protected function getModuleList() {
    $this->modules = array();
    $result = db_query("SELECT name, filename, info FROM {system} WHERE type = 'module' AND status = 1 ORDER BY weight ASC, filename ASC");
    foreach ($result as $module) {
      if (file_exists($module->filename) && function_exists($module->name . '_help')) {
        $fullname = unserialize($module->info);
        $this->modules[$module->name] = $fullname['name'];
      }
    }
  }
```

---
_Drupal 7.103 · [modules/help/help.test](https://github.com/drupal/drupal/blob/7.103/modules/help/help.test) · Licensed GPL-2.0-or-later (see LICENSE)._
