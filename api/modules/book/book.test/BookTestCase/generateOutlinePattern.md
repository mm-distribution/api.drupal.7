# BookTestCase::generateOutlinePattern()

- **Type:** Method
- **File:** [`modules/book/book.test`](../_file.md), lines 210–217 · [local source](../../../../../source/modules/book/book.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.test#L210-L217)
- **Class:** [BookTestCase](../BookTestCase.md)
- **Module/theme:** book

## Signature

```php
function generateOutlinePattern($nodes)
```

## Documentation

```text
Creates a regular expression to check for the sub-nodes in the outline.

@param array $nodes
  An array of nodes to check in outline.

@return
  A regular expression that locates sub-nodes of the outline.
```

## Code

```php
  function generateOutlinePattern($nodes) {
    $outline = '';
    foreach ($nodes as $node) {
      $outline .= '(node\/' . $node->nid . ')(.*?)(' . $node->title . ')(.*?)';
    }

    return '/<div id="book-navigation-' . $this->book->nid . '"(.*?)<ul(.*?)' . $outline . '<\/ul>/s';
  }
```

---
_Drupal 7.103 · [modules/book/book.test](https://github.com/drupal/drupal/blob/7.103/modules/book/book.test) · Licensed GPL-2.0-or-later (see LICENSE)._
