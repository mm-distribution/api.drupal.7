# TranslationTestCase::findContentByXPath()

- **Type:** Method
- **File:** [`modules/translation/translation.test`](../_file.md), lines 478–493 · [local source](../../../../../source/modules/translation/translation.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test#L478-L493)
- **Class:** [TranslationTestCase](../TranslationTestCase.md)
- **Module/theme:** translation

## Signature

```php
function findContentByXPath($xpath, array $arguments = array(), $value = NULL)
```

## Documentation

```text
Searches for elements matching the given xpath and value.

@param $xpath
  The XPath used to find the element.
@param array $arguments
  An array of arguments with keys in the form ':name' matching the
  placeholders in the query. The values may be either strings or numeric
  values.
@param $value
  The text content of the matched element to assert.

@return
  TRUE if found, otherwise FALSE.
```

## Code

```php
  function findContentByXPath($xpath, array $arguments = array(), $value = NULL) {
    $elements = $this->xpath($xpath, $arguments);

    $found = TRUE;
    if ($value && $elements) {
      $found = FALSE;
      foreach ($elements as $element) {
        if ((string) $element == $value) {
          $found = TRUE;
          break;
        }
      }
    }

    return $elements && $found;
  }
```

---
_Drupal 7.103 · [modules/translation/translation.test](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test) · Licensed GPL-2.0-or-later (see LICENSE)._
