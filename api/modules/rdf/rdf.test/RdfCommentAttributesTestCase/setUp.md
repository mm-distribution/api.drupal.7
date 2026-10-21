# RdfCommentAttributesTestCase::setUp()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 429–453 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L429-L453)
- **Class:** [RdfCommentAttributesTestCase](../RdfCommentAttributesTestCase.md)
- **Module/theme:** rdf

## Signature

```php
public function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  public function setUp() {
    parent::setUp('comment', 'rdf', 'rdf_test');

    $this->admin_user = $this->drupalCreateUser(array('administer content types', 'administer comments', 'administer permissions', 'administer blocks'));
    $this->web_user = $this->drupalCreateUser(array('access comments', 'post comments', 'create article content', 'access user profiles'));

    // Enables anonymous user comments.
    user_role_change_permissions(DRUPAL_ANONYMOUS_RID, array(
      'access comments' => TRUE,
      'post comments' => TRUE,
      'skip comment approval' => TRUE,
    ));
    // Allows anonymous to leave their contact information.
    $this->setCommentAnonymous(COMMENT_ANONYMOUS_MAY_CONTACT);
    $this->setCommentPreview(DRUPAL_OPTIONAL);
    $this->setCommentForm(TRUE);
    $this->setCommentSubject(TRUE);
    $this->setCommentSettings('comment_default_mode', COMMENT_MODE_THREADED, 'Comment paging changed.');

    // Creates the nodes on which the test comments will be posted.
    $this->drupalLogin($this->web_user);
    $this->node1 = $this->drupalCreateNode(array('type' => 'article', 'promote' => 1));
    $this->node2 = $this->drupalCreateNode(array('type' => 'article', 'promote' => 1));
    $this->drupalLogout();
  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._
