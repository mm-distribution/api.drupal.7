# TranslationTestCase::assertContentByXPath()

- **Type:** Method
- **File:** [`modules/translation/translation.test`](../_file.md), lines 404–407 · [local source](../../../../../source/modules/translation/translation.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test#L404-L407)
- **Class:** [TranslationTestCase](../TranslationTestCase.md)
- **Module/theme:** translation

## Signature

```php
function assertContentByXPath($xpath, array $arguments = array(), $value = NULL, $message = '', $group = 'Other')
```

## Documentation

```text
Asserts an element identified by the given XPath has the given content.

@param $xpath
  The XPath used to find the element.
@param array $arguments
  An array of arguments with keys in the form ':name' matching the
  placeholders in the query. The values may be either strings or numeric
  values.
@param $value
  The text content of the matched element to assert.
@param $message
  The message to display.
@param $group
  The group this message belongs to.

@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  function assertContentByXPath($xpath, array $arguments = array(), $value = NULL, $message = '', $group = 'Other') {
    $found = $this->findContentByXPath($xpath, $arguments, $value);
    return $this->assertTrue($found, $message, $group);
  }
```

---
_Drupal 7.103 · [modules/translation/translation.test](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test) · Licensed GPL-2.0-or-later (see LICENSE)._
