# ModuleVersionTestCase::testModuleVersions()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 620–659 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L620-L659)
- **Class:** [ModuleVersionTestCase](../ModuleVersionTestCase.md)
- **Module/theme:** system

## Signature

```php
function testModuleVersions()
```

## Documentation

```text
Test version dependencies.
```

## Code

```php
  function testModuleVersions() {
    $dependencies = array(
      // Alternating between being compatible and incompatible with 7.x-2.4-beta3.
      // The first is always a compatible.
      'common_test',
      // Branch incompatibility.
      'common_test (1.x)',
      // Branch compatibility.
      'common_test (2.x)',
      // Another branch incompatibility.
      'common_test (>2.x)',
      // Another branch compatibility.
      'common_test (<=2.x)',
      // Another branch incompatibility.
      'common_test (<2.x)',
      // Another branch compatibility.
      'common_test (>=2.x)',
      // Nonsense, misses a dash. Incompatible with everything.
      'common_test (=7.x2.x, >=2.4)',
      // Core version is optional. Compatible.
      'common_test (=7.x-2.x, >=2.4-alpha2)',
      // Test !=, explicitly incompatible.
      'common_test (=2.x, !=2.4-beta3)',
      // Three operations. Compatible.
      'common_test (=2.x, !=2.3, <2.5)',
      // Testing extra version. Incompatible.
      'common_test (<=2.4-beta2)',
      // Testing extra version. Compatible.
      'common_test (>2.4-beta2)',
      // Testing extra version. Incompatible.
      'common_test (>2.4-rc0)',
    );
    variable_set('dependencies', $dependencies);
    $n = count($dependencies);
    for ($i = 0; $i < $n; $i++) {
      $this->drupalGet('admin/modules');
      $checkbox = $this->xpath('//input[@id="edit-modules-testing-module-test-enable"]');
      $this->assertEqual(!empty($checkbox[0]['disabled']), $i % 2, $dependencies[$i]);
    }
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
