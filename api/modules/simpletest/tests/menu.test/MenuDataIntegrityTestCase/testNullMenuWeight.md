# MenuDataIntegrityTestCase::testNullMenuWeight()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 1763–1781 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L1763-L1781)
- **Class:** [MenuDataIntegrityTestCase](../MenuDataIntegrityTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testNullMenuWeight()
```

## Documentation

```text
Tests for null/casting weight parameter.
```

## Code

```php
  public function testNullMenuWeight() {
    $base_options = array(
      'link_title' => 'Menu link test',
      'module' => 'menu_test',
      'menu_name' => 'menu_test',
      'weight' => NULL,
      'link_path' => 'menu-test/parent',
    );

    try {
      menu_link_save($base_options);
    }
    catch (PDOException $exception) {
      $this->fail('Menu weight is not being cast properly.');
      return;
    }

    $this->pass('Menu weight is being cast properly.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
