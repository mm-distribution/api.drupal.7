# PagerFunctionalWebTestCase::assertNoClass()

- **Type:** Method
- **File:** [`modules/simpletest/tests/pager.test`](../_file.md), lines 169–174 · [local source](../../../../../../source/modules/simpletest/tests/pager.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/pager.test#L169-L174)
- **Class:** [PagerFunctionalWebTestCase](../PagerFunctionalWebTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function assertNoClass(SimpleXMLElement $element, $class, $message = NULL)
```

## Documentation

```text
Asserts that an element does not have a given class.

@param SimpleXMLElement $element
  The element to test.
@param string $class
  The class to assert.
@param string $message
  (optional) A verbose message to output.
```

## Code

```php
  protected function assertNoClass(SimpleXMLElement $element, $class, $message = NULL) {
    if (!isset($message)) {
      $message = "Class .$class not found.";
    }
    $this->assertTrue(strpos((string) $element['class'], $class) === FALSE, $message);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/pager.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/pager.test) · Licensed GPL-2.0-or-later (see LICENSE)._
