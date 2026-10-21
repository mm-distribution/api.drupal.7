# filter_dom_load()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 1106–1112 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L1106-L1112)
- **Module/theme:** filter

## Signature

```php
function filter_dom_load($text)
```

## Documentation

```text
Parses an HTML snippet and returns it as a DOM object.

This function loads the body part of a partial (X)HTML document and returns
a full DOMDocument object that represents this document. You can use
filter_dom_serialize() to serialize this DOMDocument back to a XHTML
snippet.

@param $text
  The partial (X)HTML snippet to load. Invalid mark-up will be corrected on
  import.
@return
  A DOMDocument that represents the loaded (X)HTML snippet.
```

## Code

```php
function filter_dom_load($text) {
  $dom_document = new DOMDocument();
  // Ignore warnings during HTML soup loading.
  @$dom_document->loadHTML('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head><body>' . $text . '</body></html>');

  return $dom_document;
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
