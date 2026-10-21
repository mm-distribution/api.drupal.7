# MenuRouterTestCase::testExoticPath()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 194–200 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L194-L200)
- **Class:** [MenuRouterTestCase](../MenuRouterTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testExoticPath()
```

## Documentation

```text
Test path containing "exotic" characters.
```

## Code

```php
  function testExoticPath() {
    $path = "menu-test/ -._~!$'\"()*@[]?&+%#,;=:" . // "Special" ASCII characters.
      "%23%25%26%2B%2F%3F" . // Characters that look like a percent-escaped string.
      "éøïвβ中國書۞"; // Characters from various non-ASCII alphabets.
    $this->drupalGet($path);
    $this->assertRaw('This is menu_test_callback().');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
