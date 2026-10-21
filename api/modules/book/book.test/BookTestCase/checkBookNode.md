# BookTestCase::checkBookNode()

- **Type:** Method
- **File:** [`modules/book/book.test`](../_file.md), lines 149–199 · [local source](../../../../../source/modules/book/book.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.test#L149-L199)
- **Class:** [BookTestCase](../BookTestCase.md)
- **Module/theme:** book

## Signature

```php
function checkBookNode($node, $nodes = NULL, $previous = FALSE, $up = FALSE, $next = FALSE, array $breadcrumb = array())
```

## Documentation

```text
Checks the outline of sub-pages; previous, up, and next.

Also checks the printer friendly version of the outline.

@param $node
  Node to check.
@param $nodes
  Nodes that should be in outline.
@param $previous
  (optional) Previous link node. Defaults to FALSE.
@param $up
  (optional) Up link node. Defaults to FALSE.
@param $next
  (optional) Next link node. Defaults to FALSE.
@param $breadcrumb
  (optional) The nodes that should be displayed in the breadcrumb.
```

## Code

```php
  function checkBookNode($node, $nodes = NULL, $previous = FALSE, $up = FALSE, $next = FALSE, array $breadcrumb = array()) {
    // $number does not use drupal_static as it should not be reset
    // since it uniquely identifies each call to checkBookNode().
    static $number = 0;
    $this->drupalGet('node/' . $node->nid);

    // Check outline structure.
    if ($nodes !== NULL) {
      $this->assertPattern($this->generateOutlinePattern($nodes), format_string('Node %number outline confirmed.', array('%number' => $number)));
    }
    else {
      $this->pass(format_string('Node %number does not have outline.', array('%number' => $number)));
    }

    // Check previous, up, and next links.
    if ($previous) {
      $this->assertRaw(l('‹ ' . $previous->title, 'node/' . $previous->nid, array('attributes' => array('class' => array('page-previous'), 'title' => t('Go to previous page')))), 'Previous page link found.');
    }

    if ($up) {
      $this->assertRaw(l('up', 'node/' . $up->nid, array('attributes' => array('class' => array('page-up'), 'title' => t('Go to parent page')))), 'Up page link found.');
    }

    if ($next) {
      $this->assertRaw(l($next->title . ' ›', 'node/' . $next->nid, array('attributes' => array('class' => array('page-next'), 'title' => t('Go to next page')))), 'Next page link found.');
    }

    // Compute the expected breadcrumb.
    $expected_breadcrumb = array();
    $expected_breadcrumb[] = url('');
    foreach ($breadcrumb as $a_node) {
      $expected_breadcrumb[] = url('node/' . $a_node->nid);
    }

    // Fetch links in the current breadcrumb.
    $links = $this->xpath('//div[@class="breadcrumb"]/a');
    $got_breadcrumb = array();
    foreach ($links as $link) {
      $got_breadcrumb[] = (string) $link['href'];
    }

    // Compare expected and got breadcrumbs.
    $this->assertIdentical($expected_breadcrumb, $got_breadcrumb, 'The breadcrumb is correctly displayed on the page.');

    // Check printer friendly version.
    $this->drupalGet('book/export/html/' . $node->nid);
    $this->assertText($node->title, 'Printer friendly title found.');
    $this->assertRaw(check_markup($node->body[LANGUAGE_NONE][0]['value'], $node->body[LANGUAGE_NONE][0]['format']), 'Printer friendly body found.');

    $number++;
  }
```

---
_Drupal 7.103 · [modules/book/book.test](https://github.com/drupal/drupal/blob/7.103/modules/book/book.test) · Licensed GPL-2.0-or-later (see LICENSE)._
