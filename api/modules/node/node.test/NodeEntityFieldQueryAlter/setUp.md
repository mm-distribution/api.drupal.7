# NodeEntityFieldQueryAlter::setUp()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 2481–2502 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2481-L2502)
- **Class:** [NodeEntityFieldQueryAlter](../NodeEntityFieldQueryAlter.md)
- **Module/theme:** node

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('node_access_test');
    node_access_rebuild();

    // Creating 4 nodes with an entity field so we can test that sort of query
    // alter. All field values starts with 'A' so we can identify and fetch them
    // in the node_access_test module.
    $settings = array('language' => LANGUAGE_NONE);
    for ($i = 0; $i < 4; $i++) {
      $body = array(
        'value' => 'A' . $this->randomName(32),
        'format' => filter_default_format(),
      );
      $settings['body'][LANGUAGE_NONE][0] = $body;
      $this->drupalCreateNode($settings);
    }

    // Create user with simple node access permission. The 'node test view'
    // permission is implemented and granted by the node_access_test module.
    $this->accessUser = $this->drupalCreateUser(array('access content', 'node test view'));
    $this->noAccessUser = $this->drupalCreateUser(array('access content'));
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
