# TrackerTest::setUp()

- **Type:** Method
- **File:** [`modules/tracker/tracker.test`](../_file.md), lines 35–44 · [local source](../../../../../source/modules/tracker/tracker.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.test#L35-L44)
- **Class:** [TrackerTest](../TrackerTest.md)
- **Module/theme:** tracker

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('comment', 'tracker');

    $permissions = array('access comments', 'create page content', 'post comments', 'skip comment approval');
    $this->user = $this->drupalCreateUser($permissions);
    $this->other_user = $this->drupalCreateUser($permissions);

    // Make node preview optional.
    variable_set('comment_preview_page', 0);
  }
```

---
_Drupal 7.103 · [modules/tracker/tracker.test](https://github.com/drupal/drupal/blob/7.103/modules/tracker/tracker.test) · Licensed GPL-2.0-or-later (see LICENSE)._
