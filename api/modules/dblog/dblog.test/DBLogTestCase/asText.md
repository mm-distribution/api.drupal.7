# DBLogTestCase::asText()

- **Type:** Method
- **File:** [`modules/dblog/dblog.test`](../_file.md), lines 690–695 · [local source](../../../../../source/modules/dblog/dblog.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test#L690-L695)
- **Class:** [DBLogTestCase](../DBLogTestCase.md)
- **Module/theme:** dblog

## Signature

```php
protected function asText(SimpleXMLElement $element)
```

## Documentation

```text
Extracts the text contained by the XHTML element.

@param SimpleXMLElement $element
  Element to extract text from.

@return string
  Extracted text.
```

## Code

```php
  protected function asText(SimpleXMLElement $element) {
    if (!is_object($element)) {
      return $this->fail('The element is not an element.');
    }
    return trim(html_entity_decode(strip_tags($element->asXML())));
  }
```

---
_Drupal 7.103 · [modules/dblog/dblog.test](https://github.com/drupal/drupal/blob/7.103/modules/dblog/dblog.test) · Licensed GPL-2.0-or-later (see LICENSE)._
