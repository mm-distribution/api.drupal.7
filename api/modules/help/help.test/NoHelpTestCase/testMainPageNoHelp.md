# NoHelpTestCase::testMainPageNoHelp()

- **Type:** Method
- **File:** [`modules/help/help.test`](../_file.md), lines 136–141 · [local source](../../../../../source/modules/help/help.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/help/help.test#L136-L141)
- **Class:** [NoHelpTestCase](../NoHelpTestCase.md)
- **Module/theme:** help

## Signature

```php
function testMainPageNoHelp()
```

## Documentation

```text
Ensures modules not implementing help do not appear on admin/help.
```

## Code

```php
  function testMainPageNoHelp() {
    $this->drupalLogin($this->big_user);

    $this->drupalGet('admin/help');
    $this->assertNoText('Hook menu tests', 'Making sure the test module menu_test does not display a help link in admin/help');
  }
```

---
_Drupal 7.103 · [modules/help/help.test](https://github.com/drupal/drupal/blob/7.103/modules/help/help.test) · Licensed GPL-2.0-or-later (see LICENSE)._
