# UpdateScriptFunctionalTest::testThemeSystem()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2631–2640 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2631-L2640)
- **Class:** [UpdateScriptFunctionalTest](../UpdateScriptFunctionalTest.md)
- **Module/theme:** system

## Signature

```php
function testThemeSystem()
```

## Documentation

```text
Tests the effect of using the update script on the theme system.
```

## Code

```php
  function testThemeSystem() {
    // Since visiting update.php triggers a rebuild of the theme system from an
    // unusual maintenance mode environment, we check that this rebuild did not
    // put any incorrect information about the themes into the database.
    $original_theme_data = db_query("SELECT * FROM {system} WHERE type = 'theme' ORDER BY name")->fetchAll();
    $this->drupalLogin($this->update_user);
    $this->drupalGet($this->update_url, array('external' => TRUE));
    $final_theme_data = db_query("SELECT * FROM {system} WHERE type = 'theme' ORDER BY name")->fetchAll();
    $this->assertEqual($original_theme_data, $final_theme_data, 'Visiting update.php does not alter the information about themes stored in the database.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
