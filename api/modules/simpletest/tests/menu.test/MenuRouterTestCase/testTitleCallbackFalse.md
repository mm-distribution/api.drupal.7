# MenuRouterTestCase::testTitleCallbackFalse()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 146–150 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L146-L150)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testTitleCallbackFalse()
```

## Documentation

```text
Test title callback set to FALSE.
```

## Code

```php
  function testTitleCallbackFalse() {
    $this->drupalGet('node');
    $this->assertText('A title with @placeholder', 'Raw text found on the page');
    $this->assertNoText(t('A title with @placeholder', array('@placeholder' => 'some other text')), 'Text with placeholder substitutions not found.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
