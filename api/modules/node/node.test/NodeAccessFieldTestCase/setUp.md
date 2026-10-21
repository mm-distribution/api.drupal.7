# NodeAccessFieldTestCase::setUp()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 2872–2888 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2872-L2888)
- **Class:** [NodeAccessFieldTestCase](../NodeAccessFieldTestCase.md)
- **Module/theme:** node

## Signature

```php
public function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  public function setUp() {
    parent::setUp('node_access_test', 'field_ui');
    node_access_rebuild();

    // Create some users.
    $this->admin_user = $this->drupalCreateUser(array('access content', 'bypass node access', 'administer fields'));
    $this->content_admin_user = $this->drupalCreateUser(array('access content', 'administer content types', 'administer fields'));

    // Add a custom field to the page content type.
    $this->field_name = drupal_strtolower($this->randomName() . '_field_name');
    $this->field = field_create_field(array('field_name' => $this->field_name, 'type' => 'text'));
    $this->instance = field_create_instance(array(
      'field_name' => $this->field_name,
      'entity_type' => 'node',
      'bundle' => 'page',
    ));
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
