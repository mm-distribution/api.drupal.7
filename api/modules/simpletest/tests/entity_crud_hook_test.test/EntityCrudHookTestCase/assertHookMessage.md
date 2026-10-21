# EntityCrudHookTestCase::assertHookMessage()

- **Type:** Method
- **File:** [`modules/simpletest/tests/entity_crud_hook_test.test`](../_file.md), lines 49–54 · [local source](../../../../../../source/modules/simpletest/tests/entity_crud_hook_test.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.test#L49-L54)
- **Class:** [EntityCrudHookTestCase](../EntityCrudHookTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function assertHookMessage($text, $message = NULL, $group = 'Other')
```

## Documentation

```text
Pass if the message $text was set by one of the CRUD hooks in
entity_crud_hook_test.module, i.e., if the $text is an element of
$_SESSION['entity_crud_hook_test'].

@param $text
  Plain text to look for.
@param $message
  Message to display.
@param $group
  The group this message belongs to, defaults to 'Other'.
@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  protected function assertHookMessage($text, $message = NULL, $group = 'Other') {
    if (!isset($message)) {
      $message = $text;
    }
    return $this->assertTrue(array_search($text, $_SESSION['entity_crud_hook_test']) !== FALSE, $message, $group);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud_hook_test.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud_hook_test.test) · Licensed GPL-2.0-or-later (see LICENSE)._
