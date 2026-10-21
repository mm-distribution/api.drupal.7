# Ajax framework

- **Topic id:** `ajax`
- **Defined in:** [`includes/ajax.inc`](../includes/ajax.inc/_file.md), line 8 · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/ajax.inc#L8)

## Documentation

```text
@defgroup ajax Ajax framework
@{
Functions for Drupal's Ajax framework.

Drupal's Ajax framework is used to dynamically update parts of a page's HTML
based on data from the server. Upon a specified event, such as a button
click, a callback function is triggered which performs server-side logic and
may return updated markup, which is then replaced on-the-fly with no page
refresh necessary.

This framework creates a PHP macro language that allows the server to
instruct JavaScript to perform actions on the client browser. When using
forms, it can be used with the #ajax property.
The #ajax property can be used to bind events to the Ajax framework. By
default, #ajax uses 'system/ajax' as its path for submission and thus calls
ajax_form_callback() and a defined #ajax['callback'] function.
However, you may optionally specify a different path to request or a
different callback function to invoke, which can return updated HTML or can
also return a richer set of
@link ajax_commands Ajax framework commands @endlink.

Standard form handling is as follows:
  - A form element has a #ajax property that includes #ajax['callback'] and
    omits #ajax['path']. See below about using #ajax['path'] to implement
    advanced use-cases that require something other than standard form
    handling.
  - On the specified element, Ajax processing is triggered by a change to
    that element.
  - The browser submits an HTTP POST request to the 'system/ajax' Drupal
    path.
  - The menu page callback for 'system/ajax', ajax_form_callback(), calls
    drupal_process_form() to process the form submission and rebuild the
    form if necessary. The form is processed in much the same way as if it
    were submitted without Ajax, with the same #process functions and
    validation and submission handlers called in either case, making it easy
    to create Ajax-enabled forms that degrade gracefully when JavaScript is
    disabled.
  - After form processing is complete, ajax_form_callback() calls the
    function named by #ajax['callback'], which returns the form element that
    has been updated and needs to be returned to the browser, or
    alternatively, an array of custom Ajax commands.
  - The page delivery callback for 'system/ajax', ajax_deliver(), renders the
    element returned by #ajax['callback'], and returns the JSON string
    created by ajax_render() to the browser.
  - The browser unserializes the returned JSON string into an array of
    command objects and executes each command, resulting in the old page
    content within and including the HTML element specified by
    #ajax['wrapper'] being replaced by the new content returned by
    #ajax['callback'], using a JavaScript animation effect specified by
    #ajax['effect'].

A simple example of basic Ajax use from the
@link http://drupal.org/project/examples Examples module @endlink follows:
@code
function main_page() {
  return drupal_get_form('ajax_example_simplest');
}

function ajax_example_simplest($form, &$form_state) {
  $form = array();
  $form['changethis'] = array(
    '#type' => 'select',
    '#options' => array(
      'one' => 'one',
      'two' => 'two',
      'three' => 'three',
    ),
    '#ajax' => array(
      'callback' => 'ajax_example_simplest_callback',
      'wrapper' => 'replace_textfield_div',
     ),
  );

  // This entire form element will be replaced with an updated value.
  $form['replace_textfield'] = array(
    '#type' => 'textfield',
    '#title' => t("The default value will be changed"),
    '#description' => t("Say something about why you chose") . "'" .
      (!empty($form_state['values']['changethis'])
      ? $form_state['values']['changethis'] : t("Not changed yet")) . "'",
    '#prefix' => '<div id="replace_textfield_div">',
    '#suffix' => '</div>',
  );
  return $form;
}

function ajax_example_simplest_callback($form, $form_state) {
  // The form has already been submitted and updated. We can return the replaced
  // item as it is.
  return $form['replace_textfield'];
}
@endcode

In the above example, the 'changethis' element is Ajax-enabled. The default
#ajax['event'] is 'change', so when the 'changethis' element changes,
an Ajax call is made. The form is submitted and reprocessed, and then the
callback is called. In this case, the form has been automatically
built changing $form['replace_textfield']['#description'], so the callback
just returns that part of the form.

To implement Ajax handling in a form, add '#ajax' to the form
definition of a field. That field will trigger an Ajax event when it is
clicked (or changed, depending on the kind of field). #ajax supports
the following parameters (either 'path' or 'callback' is required at least):
- #ajax['callback']: The callback to invoke to handle the server side of the
  Ajax event, which will receive a $form and $form_state as arguments, and
  returns a renderable array (most often a form or form fragment), an HTML
  string, or an array of Ajax commands. If returning a renderable array or
  a string, the value will replace the original element named in
  #ajax['wrapper'], and
  theme_status_messages()
  will be prepended to that
  element. (If the status messages are not wanted, return an array
  of Ajax commands instead.)
  #ajax['wrapper']. If an array of Ajax commands is returned, it will be
  executed by the calling code.
- #ajax['path']: The menu path to use for the request. This is often omitted
  and the default is used. This path should map
  to a menu page callback that returns data using ajax_render(). Defaults to
  'system/ajax', which invokes ajax_form_callback(), eventually calling
  the function named in #ajax['callback']. If you use a custom
  path, you must set up the menu entry and handle the entire callback in your
  own code.
- #ajax['wrapper']: The CSS ID of the area to be replaced by the content
  returned by the #ajax['callback'] function. The content returned from
  the callback will replace the entire element named by #ajax['wrapper'].
  The wrapper is usually created using #prefix and #suffix properties in the
  form. Note that this is the wrapper ID, not a CSS selector. So to replace
  the element referred to by the CSS selector #some-selector on the page,
  use #ajax['wrapper'] = 'some-selector', not '#some-selector'.
- #ajax['effect']: The jQuery effect to use when placing the new HTML.
  Defaults to no effect. Valid options are 'none', 'slide', or 'fade'.
- #ajax['speed']: The effect speed to use. Defaults to 'slow'. May be
  'slow', 'fast' or a number in milliseconds which represents the length
  of time the effect should run.
- #ajax['event']: The JavaScript event to respond to. This is normally
  selected automatically for the type of form widget being used, and
  is only needed if you need to override the default behavior.
- #ajax['prevent']: A JavaScript event to prevent when 'event' is triggered.
  Defaults to 'click' for #ajax on #type 'submit', 'button', and
  'image_button'. Multiple events may be specified separated by spaces.
  For example, when binding #ajax behaviors to form buttons, pressing the
  ENTER key within a textfield triggers the 'click' event of the form's first
  submit button. Triggering Ajax in this situation leads to problems, like
  breaking autocomplete textfields. Because of that, Ajax behaviors are bound
  to the 'mousedown' event on form buttons by default. However, binding to
  'mousedown' rather than 'click' means that it is possible to trigger a
  click by pressing the mouse, holding the mouse button down until the Ajax
  request is complete and the button is re-enabled, and then releasing the
  mouse button. For this case, 'prevent' can be set to 'click', so an
  additional event handler is bound to prevent such a click from triggering a
  non-Ajax form submission. This also prevents a textfield's ENTER press
  triggering a button's non-Ajax form submission behavior.
- #ajax['method']: The jQuery method to use to place the new HTML.
  Defaults to 'replaceWith'. May be: 'replaceWith', 'append', 'prepend',
  'before', 'after', or 'html'. See the
  @link http://api.jquery.com/category/manipulation/ jQuery manipulators documentation @endlink
  for more information on these methods.
- #ajax['progress']: Choose either a throbber or progress bar that is
  displayed while awaiting a response from the callback, and add an optional
  message. Possible keys: 'type', 'message', 'url', 'interval'.
  More information is available in the
  @link forms_api_reference.html Form API Reference @endlink

In addition to using Form API for doing in-form modification, Ajax may be
enabled by adding classes to buttons and links. By adding the 'use-ajax'
class to a link, the link will be loaded via an Ajax call. When using this
method, the href of the link can contain '/nojs/' as part of the path. When
the Ajax framework makes the request, it will convert this to '/ajax/'.
The server is then able to easily tell if this request was made through an
actual Ajax request or in a degraded state, and respond appropriately.

Similarly, submit buttons can be given the class 'use-ajax-submit'. The
form will then be submitted via Ajax to the path specified in the #action.
Like the ajax-submit class above, this path will have '/nojs/' replaced with
'/ajax/' so that the submit handler can tell if the form was submitted
in a degraded state or not.

When responding to Ajax requests, the server should do what it needs to do
for that request, then create a commands array. This commands array will
be converted to a JSON object and returned to the client, which will then
iterate over the array and process it like a macro language.

Each command item is an associative array which will be converted to a
command object on the JavaScript side. $command_item['command'] is the type
of command, e.g. 'alert' or 'replace', and will correspond to a method in the
Drupal.ajax[command] space. The command array may contain any other data that
the command needs to process, e.g. 'method', 'selector', 'settings', etc.

Commands are usually created with a couple of helper functions, so they
look like this:
@code
  $commands = array();
  // Replace the content of '#object-1' on the page with 'some html here'.
  $commands[] = ajax_command_replace('#object-1', 'some html here');
  // Add a visual "changed" marker to the '#object-1' element.
  $commands[] = ajax_command_changed('#object-1');
  // Menu 'page callback' and #ajax['callback'] functions are supposed to
  // return render arrays. If returning an Ajax commands array, it must be
  // encapsulated in a render array structure.
  return array('#type' => 'ajax', '#commands' => $commands);
@endcode

When returning an Ajax command array, it is often useful to have
status messages rendered along with other tasks in the command array.
In that case the Ajax commands array may be constructed like this:
@code
  $commands = array();
  $commands[] = ajax_command_replace(NULL, $output);
  $commands[] = ajax_command_prepend(NULL, theme('status_messages'));
  return array('#type' => 'ajax', '#commands' => $commands);
@endcode

See @link ajax_commands Ajax framework commands @endlink
```

## Members (derived, 10)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [ajax_base_page_theme()](../includes/ajax.inc/ajax_base_page_theme.md) (function) — Theme callback for Ajax requests.
- [ajax_deliver()](../includes/ajax.inc/ajax_deliver.md) (function) — Packages and sends the result of a page callback as an Ajax response.
- [ajax_footer()](../includes/ajax.inc/ajax_footer.md) (function) — Performs end-of-Ajax-request tasks.
- [ajax_form_callback()](../includes/ajax.inc/ajax_form_callback.md) (function) — Menu callback; handles Ajax requests for the #ajax Form API property.
- [ajax_get_form()](../includes/ajax.inc/ajax_get_form.md) (function) — Gets a form submitted via #ajax during an Ajax callback.
- [ajax_pre_render_element()](../includes/ajax.inc/ajax_pre_render_element.md) (function) — Adds Ajax information about an element to communicate with JavaScript.
- [ajax_prepare_response()](../includes/ajax.inc/ajax_prepare_response.md) (function) — Converts the return value of a page callback into an Ajax commands array.
- [ajax_process_form()](../includes/ajax.inc/ajax_process_form.md) (function) — Form element processing handler for the #ajax form property.
- [ajax_render()](../includes/ajax.inc/ajax_render.md) (function) — Renders a commands array into JSON.
- [ajax_set_verification_header()](../includes/ajax.inc/ajax_set_verification_header.md) (function) — Sets a response header for ajax.js to trust the response body.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
