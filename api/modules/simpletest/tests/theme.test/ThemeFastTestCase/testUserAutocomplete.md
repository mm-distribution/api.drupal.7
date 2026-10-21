# ThemeFastTestCase::testUserAutocomplete()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 452–456 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L452-L456)
- **Class:** [ThemeFastTestCase](../ThemeFastTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testUserAutocomplete()
```

## Documentation

```text
Tests access to user autocompletion and verify the correct results.
```

## Code

```php
  function testUserAutocomplete() {
    $this->drupalLogin($this->account);
    $this->drupalGet('user/autocomplete/' . $this->account->name);
    $this->assertText('registry not initialized', 'The registry was not initialized');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
