# FilterDOMSerializeTestCase::testFilterEmptyDOMSerialization()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 2073–2077 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L2073-L2077)
- **Class:** [FilterDOMSerializeTestCase](../FilterDOMSerializeTestCase.md)
- **Module/theme:** filter

## Signature

```php
function testFilterEmptyDOMSerialization()
```

## Documentation

```text
Tests empty DOMDocument object.
```

## Code

```php
  function testFilterEmptyDOMSerialization() {
    $document = new DOMDocument();
    $result = filter_dom_serialize($document);
    $this->assertEqual('', $result);
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
