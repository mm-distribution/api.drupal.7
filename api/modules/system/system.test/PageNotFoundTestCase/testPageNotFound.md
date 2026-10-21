# PageNotFoundTestCase::testPageNotFound()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1158–1178 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1158-L1178)
- **Class:** [PageNotFoundTestCase](../PageNotFoundTestCase.md)
- **Module/theme:** system

## Signature

```php
function testPageNotFound()
```

## Documentation

_No docblock in source._

## Code

```php
  function testPageNotFound() {
    $this->drupalGet($this->randomName(10));
    $this->assertText(t('Page not found'), 'Found the default 404 page');

    $edit = array(
      'title' => $this->randomName(10),
      'body' => array(LANGUAGE_NONE => array(array('value' => $this->randomName(100)))),
    );
    $node = $this->drupalCreateNode($edit);

    // As node IDs must be integers, make sure requests for non-integer IDs
    // return a page not found error.
    $this->drupalGet('node/invalid');
    $this->assertResponse(404);

    // Use a custom 404 page.
    $this->drupalPost('admin/config/system/site-information', array('site_404' => 'node/' . $node->nid), t('Save configuration'));

    $this->drupalGet($this->randomName(10));
    $this->assertText($node->title, 'Found the custom 404 page');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
