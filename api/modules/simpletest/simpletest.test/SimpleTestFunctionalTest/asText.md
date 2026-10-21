# SimpleTestFunctionalTest::asText()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 331–336 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L331-L336)
- **Class:** [SimpleTestFunctionalTest](../SimpleTestFunctionalTest.md)
- **Module/theme:** simpletest

## Signature

```php
function asText(SimpleXMLElement $element)
```

## Documentation

```text
Extract the text contained by the element.

@param $element
  Element to extract text from.
@return
  Extracted text.
```

## Code

```php
  function asText(SimpleXMLElement $element) {
    if (!is_object($element)) {
      return $this->fail('The element is not an element.');
    }
    return trim(html_entity_decode(strip_tags($element->asXML())));
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
