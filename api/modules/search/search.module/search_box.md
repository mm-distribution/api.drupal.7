# search_box()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 1009–1023 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L1009-L1023)
- **Module/theme:** search
- **Topics:** [search](../../../topics/search.md), [forms](../../../topics/forms.md)

## Signature

```php
function search_box($form, &$form_state, $form_id)
```

## Documentation

```text
Form builder; Output a search form for the search block's search box.

@ingroup forms
@see search_box_form_submit()
@see search-block-form.tpl.php
```

## Code

```php
function search_box($form, &$form_state, $form_id) {
  $form[$form_id] = array(
    '#type' => 'textfield',
    '#title' => t('Search'),
    '#title_display' => 'invisible',
    '#size' => 15,
    '#default_value' => '',
    '#attributes' => array('title' => t('Enter the terms you wish to search for.')),
  );
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array('#type' => 'submit', '#value' => t('Search'));
  $form['#submit'][] = 'search_box_form_submit';

  return $form;
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
