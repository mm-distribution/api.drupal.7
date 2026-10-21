# CommentInterfaceTest::testCommentLinks()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 682–712 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L682-L712)
- **Class:** [CommentInterfaceTest](../CommentInterfaceTest.md)
- **Module/theme:** comment

## Signature

```php
function testCommentLinks()
```

## Documentation

```text
Tests comment links.

The output of comment links depends on various environment conditions:
- Various Comment module configuration settings, user registration
  settings, and user access permissions.
- Whether the user is authenticated or not, and whether any comments exist.

To account for all possible cases, this test creates permutations of all
possible conditions and tests the expected appearance of comment links in
each environment.
```

## Code

```php
  function testCommentLinks() {
    // Bartik theme alters comment links, so use a different theme.
    theme_enable(array('garland'));
    variable_set('theme_default', 'garland');

    // Remove additional user permissions from $this->web_user added by setUp(),
    // since this test is limited to anonymous and authenticated roles only.
    user_role_delete(key($this->web_user->roles));

    // Matrix of possible environmental conditions and configuration settings.
    // See setEnvironment() for details.
    $conditions = array(
      'authenticated'   => array(FALSE, TRUE),
      'comment count'   => array(FALSE, TRUE),
      'access comments' => array(0, 1),
      'post comments'   => array(0, 1),
      'form'            => array(COMMENT_FORM_BELOW, COMMENT_FORM_SEPARATE_PAGE),
      // USER_REGISTER_VISITORS_ADMINISTRATIVE_APPROVAL is irrelevant for this
      // test; there is only a difference between open and closed registration.
      'user_register'   => array(USER_REGISTER_VISITORS, USER_REGISTER_ADMINISTRATORS_ONLY),
      // @todo Complete test coverage for:
      //'comments'        => array(COMMENT_NODE_OPEN, COMMENT_NODE_CLOSED, COMMENT_NODE_HIDDEN),
      //// COMMENT_ANONYMOUS_MUST_CONTACT is irrelevant for this test.
      //'contact '        => array(COMMENT_ANONYMOUS_MAY_CONTACT, COMMENT_ANONYMOUS_MAYNOT_CONTACT),
    );

    $environments = $this->generatePermutations($conditions);
    foreach ($environments as $info) {
      $this->assertCommentLinks($info);
    }
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
