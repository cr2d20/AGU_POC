"""
TGI POC
"""
import asyncio
import time
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER

headings = ['Customer Name', 'City', 'Req', 'Attended by']
customers = [
    ('Yuvan', 'Bengluru', 'TGI 1', 'xyz'),
    ('Rocky', 'Bengluru', 'TGI 7', 'lll'),
    ('Arohi', 'Hassan', 'TGI 6', 'xyz'),
    ('Bhanu', 'Hassan', 'TGI 10', 'wdf'),
]

class TGIPOC(toga.App):
    def startup(self):

        # agu logo
        image = toga.Image('resources/agu.png')
        self.agu_image_view = toga.ImageView(image, style=Pack(padding=10, width=300, height=300))

        # username
        username_label = toga.Label(
            'Username: ',
            style=Pack(width=300, padding=(10, 5))
        )
        self.username_input = toga.TextInput(style=Pack(width=300, flex=1))

        login_box = toga.Box(style=Pack(alignment=CENTER, direction=COLUMN, padding=5))

        login_box.add(self.agu_image_view)

        login_box.add(username_label)
        login_box.add(self.username_input)

        # password
        password_label = toga.Label(
            'Password: ',
            style=Pack(width=300, padding=(10, 5))
        )
        self.password_input = toga.PasswordInput(style=Pack(width=300, flex=1))

        login_box.add(password_label)
        login_box.add(self.password_input)

        button = toga.Button(
            'Login',
            on_press=self.home,
            style=Pack(padding_top=25, width=100)
        )

        login_box.add(button)

        self.login_main_box = toga.Box(
            children=[login_box],
            style=Pack(direction=COLUMN, padding=250, padding_top=100, alignment=CENTER, flex=1)
        )

        image1 = toga.Image('resources/RDDR.png')
        self.logo_image_view = toga.ImageView(image1, style=Pack(padding=10, width=300, height=300))

        company_logo_box = toga.Box(style=Pack(direction=COLUMN, padding=250, padding_top=100
                                               , alignment=CENTER, flex=1))
        company_logo_box.add(self.logo_image_view)

        self.main_window = toga.MainWindow(title="AGU")
        self.main_window.content = company_logo_box
        self.main_window.show()

        self.add_background_task(self.do_background_task)

    async def do_background_task(self, widget, **kwargs):
        "A background task"
        # This task runs in the background, without blocking the main event loop
        # Company logo

        await asyncio.sleep(1)
        self.main_window.content = self.login_main_box
        self.main_window.show()


    def home(self, widget):
        if self.username_input.value:
            name = self.username_input.value
        else:
            name = 'stranger'
        if self.password_input.value:
            passw = self.password_input.value
        else:
            passw = 'stranger'
        if name != "Youw0n" or passw != "Youw0n":
            self.main_window.info_dialog("Agu", "Incorrect Login!!")
            self.main_window.close()


        button = toga.Button(
            'Enter Customer details',
            on_press=self.enter_cust_details,
            style=Pack(width=300, padding=25)
        )

        button1 = toga.Button(
            'Products',
            on_press=self.products,
            style=Pack(width=300, padding=25)
        )

        button2 = toga.Button(
            'Customers',
            on_press=self.customers,
            style=Pack(width=300, padding=25)
        )

        self.main_box = toga.Box(
            children=[
                self.agu_image_view,
                button,
                button1,
                button2
            ],
            style=Pack(direction=COLUMN),
        )

        self.box = toga.Box(
            children=[],
            style=Pack(direction=COLUMN, padding=100, padding_top=100, padding_left=250, alignment=CENTER, flex=1)
        )

        # this tests adding children when we already have an impl but no window or app
        self.box.add(self.main_box)
        self.main_window.content = self.box
        self.main_window.show()


    def enter_cust_details(self, widget):
        name_label = toga.Label(
            'Customer name: ',
            style=Pack(padding=(10, 2))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        # Phone number
        phone_label = toga.Label(
            'Phone Number: ',
            style=Pack(padding=(10, 5))
        )
        self.phone_input = toga.TextInput(style=Pack(flex=1))

        phone_box = toga.Box(style=Pack(direction=ROW, padding=5))
        phone_box.add(phone_label)
        phone_box.add(self.phone_input)

        # Email
        email_label = toga.Label(
            'Email: ',
            style=Pack(padding=(10, 5))
        )
        self.email_input = toga.TextInput(style=Pack(flex=1))

        email_box = toga.Box(style=Pack(direction=ROW, padding=5))
        email_box.add(email_label)
        email_box.add(self.email_input)

        # City
        city_label = toga.Label(
            'City: ',
            style=Pack(padding=(10, 5))
        )
        self.city_input = toga.TextInput(style=Pack(flex=1))


        # Country
        country_label = toga.Label(
            'Country: ',
            style=Pack(padding=(10, 5))
        )
        self.country_input = toga.TextInput(style=Pack(flex=1))

        country_box = toga.Box(style=Pack(direction=ROW, padding=5))
        country_box.add(city_label)
        country_box.add(self.city_input)
        country_box.add(country_label)
        country_box.add(self.country_input)

        # Adress
        address_label = toga.Label(
            'Address: ',
            style=Pack(padding=(10, 5))
        )
        self.add_input = toga.MultilineTextInput(style=Pack(flex=1))

        add_box = toga.Box(style=Pack(direction=ROW, padding=5))
        add_box.add(address_label)
        add_box.add(self.add_input)

        # Requirement
        req_label = toga.Label(
            'Requirement: ',
            style=Pack(padding=(10, 5))
        )
        self.req_input = toga.MultilineTextInput(style=Pack(flex=1))

        req_box = toga.Box(style=Pack(direction=ROW, padding=5))
        req_box.add(req_label)
        req_box.add(self.req_input)

        # Nature of Business
        nob_label = toga.Label(
            'Nature of Business: ',
            style=Pack(padding=(10, 5))
        )
        self.nob_input = toga.MultilineTextInput(style=Pack(flex=1))

        nob_box = toga.Box(style=Pack(direction=ROW, padding=5))
        nob_box.add(nob_label)
        nob_box.add(self.nob_input)

        # Notes
        note_label = toga.Label(
            'Notes: ',
            style=Pack(padding=(10, 5))
        )
        self.note_input = toga.MultilineTextInput(style=Pack(flex=1))

        note_box = toga.Box(style=Pack(direction=ROW, padding=5))
        note_box.add(note_label)
        note_box.add(self.note_input)

        # Follow Up
        followup_label = toga.Label(
            'Follow Up: ',
            style=Pack(padding=(10, 5))
        )
        self.followup_input = toga.TextInput(style=Pack(flex=1))

        followup_box = toga.Box(style=Pack(direction=ROW, padding=5))
        followup_box.add(followup_label)
        followup_box.add(self.followup_input)

        button = toga.Button(
            'Save',
            on_press=self.save,
            style=Pack(padding_top=25, width=100, alignment=CENTER)
        )

        main_box = toga.Box(
            children=[
                name_box,
                phone_box,
                email_box,
                add_box,
                country_box,
                req_box,
                nob_box,
                note_box,
                button
            ],
            style=Pack(padding=50, padding_top=50, direction=COLUMN, alignment=CENTER),
        )

        self.secondary_window = toga.Window(title="New Customer details")
        self.secondary_window.content = main_box
        self.secondary_window.show()

    def save(self, widget):

       self.main_window.info_dialog("Agu",
          "Saved!"
       )

    def products(self, widget):
        main_box = toga.Box(style=Pack(padding=250, padding_top=50, direction=COLUMN, alignment=CENTER))

        name_label = toga.Label(
            'Product Name: ',
            style=Pack(padding=(10, 2))
        )
        self.product_name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.product_name_input)

        # Phone number
        phone_label = toga.Label(
            'Model Number: ',
            style=Pack(padding=(10, 5))
        )
        self.model_input = toga.TextInput(style=Pack(flex=1))

        phone_box = toga.Box(style=Pack(direction=ROW, padding=5))
        phone_box.add(phone_label)
        phone_box.add(self.model_input)

        button = toga.Button(
            'Show',
            on_press=self.get_product,
            style=Pack(padding_top=25, width=100, alignment=CENTER)
        )

        main_box.add(name_box)
        main_box.add(phone_box)
        main_box.add(button)

        self.prooduct_window = toga.Window(title="Products")
        self.prooduct_window.content = main_box
        self.prooduct_window.show()

    def get_product(self, widget):

       self.main_window.info_dialog("Agu",
         """
            Frothing nozzle : Yes
            Water protection system : no
            Dimensions of the product (mm) : 455 x
            594 x 375
            Required niche size for installation
            (HxWxD) : 449 x 558 x 354
            Hot water spout : Yes
            Adjustable programs : Brewing
            temperature, Coffee powder quantity
            per cup, Grinding factor, Water
            hardness, Water quantity per serving
            Standby function : Yes
            Pump pressure (bar) : 19
            Simultaneous preparation of 2 cups :
            Yes
            Included accessories : 9 x assembly
            screws, 1 x scoop, 1 x water filter, 1 x
            test strip, 1 x milk container (insulated),
            1 x connection hose for milk frother, 1 x
            milk pipe
            Optional accessories : HEZ860060,
            TCZ6001, TCZ7003, TC"""
       )

    def customers(self, widget):
        self.cust_window = toga.Window(title="Customer Details")

        # Data to populate the table.
        data = []
        for x in range(5):
            data.append(tuple(str(x) for x in range(5)))

        self.table1 = toga.Table(
            headings=headings,
            data=customers[:4],
            style=Pack(flex=1),
            multiple_select=False,
        )

        tablebox = toga.Box(children=[self.table1], style=Pack(flex=1))


        # Most outer box
        outer_box = toga.Box(
            children=[tablebox],
            style=Pack(
                flex=1,
                direction=COLUMN,
                padding=10,
            )
        )

        # Add the content on the main window
        self.cust_window.content = outer_box

        # Show the main window
        self.cust_window.show()


def main():
    return TGIPOC()
