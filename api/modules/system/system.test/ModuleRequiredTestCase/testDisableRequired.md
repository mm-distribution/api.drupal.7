# ModuleRequiredTestCase::testDisableRequired()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 677–693 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L677-L693)
- **Class:** [ModuleRequiredTestCase](../ModuleRequiredTestCase.md)
- **Module/theme:** system

## Signature

```php
function testDisableRequired()
```

## Documentation

```text
Assert that core required modules cannot be disabled.
```

## Code

```php
  function testDisableRequired() {
    $module_info = system_get_info('module');
    $this->drupalGet('admin/modules');
    foreach ($module_info as $module => $info) {
      // Check to make sure the checkbox for each required module is disabled
      // and checked (or absent from the page if the module is also hidden).
      if (!empty($info['required'])) {
        $field_name = "modules[{$info['package']}][$module][enable]";
        if (empty($info['hidden'])) {
          $this->assertFieldByXPath("//input[@name='$field_name' and @disabled='disabled' and @checked='checked']", '', format_string('Field @name was disabled and checked.', array('@name' => $field_name)));
        }
        else {
          $this->assertNoFieldByName($field_name);
        }
      }
    }
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
