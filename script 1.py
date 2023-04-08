from tkinter import *
from tkinter import ttk
from poke_api import get_pokemon_info
from tkinter import messagebox 

# Create the window
root = Tk()
root.title("Pokemon Information")

# Additional window configuration
root.resizable(False, False)


# frames
frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2, padx=(20, 10))
frm_btm_left = ttk.LabelFrame(root, text = 'Info')
frm_btm_left.grid(row=1, column=0, padx=(20, 10), pady=(10, 20), sticky= N)
frm_btm_right = ttk.LabelFrame(root, text = 'Stats')
frm_btm_right.grid(row=1, column=1, padx=(20, 10), pady=(10, 20), sticky= N)


#Add widgets to the frames (Without the "e" accent lol)
#populate widgets in the top frame
lbl_name = ttk.Label(frm_top, text='Pokemon Name: ')
lbl_name.grid(row=0, column=0, padx= (10, 5), pady=10)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1)

def handle():
    #get the Poke name entered by the user
    poke_name = ent_name.get().strip()
    if len(poke_name) == 0:
        #print("Please enter a Pokemon name")
        return
    
    #get the pokemon info from the PokeAPI
    poke_info = get_pokemon_info(poke_name)
    if poke_info is None:
        err_msg = f'Unable to fetch Information for {poke_name.capitalize()} from the PokeAPI.'
        messagebox.showinfo(title = 'Error', message =  err_msg, icon = 'error')
        return


    #populate the info values
    lbl_height_value['text'] = f'{poke_info["height"]} dm'
    lbl_weight_value['text'] = f'{poke_info["weight"]} hg'
    lbl_type_value['text'] = ", ".join([t['type']['name'] for t in poke_info['types']])
  

    #populate the Bar stat values
    bar_hp['value'] = poke_info['stats'][0]['base_stat']
    bar_attack['value'] = poke_info['stats'][1]['base_stat']
    bar_def['value'] = poke_info['stats'][2]['base_stat']
    bar_special_attack['value'] = poke_info['stats'][3]['base_stat']
    bar_special_def['value'] = poke_info['stats'][4]['base_stat']
    bar_speed['value'] = poke_info['stats'][5]['base_stat']
  

    return

btn_info = ttk.Button(frm_top, text='Click for Info', command = handle)
btn_info.grid(row=0, column=2, padx=10, pady = 10 )

#populate widgets in the height frame
lbl_height = ttk.Label(frm_btm_left, text='Height: ')
lbl_height.grid(row=0, column=0, padx= (10, 5), pady=(10, 5), sticky = E)

# Vallue for height
lbl_height_value = ttk.Label(frm_btm_left, text='Processing...')
lbl_height_value.grid(row=0, column=1, padx= (0, 10), pady=(10, 5), sticky = E)

#populate widgets in the Weight frame
lbl_weight = ttk.Label(frm_btm_left, text='Weight: ')
lbl_weight.grid(row=1, column=0, padx= (10, 5), pady=(10, 5), sticky = E)

# Vallue for weight
lbl_weight_value = ttk.Label(frm_btm_left, text='Processing...')
lbl_weight_value.grid(row=1, column=1, padx= (0, 10), pady=(10, 5), sticky = E)

#populate widgets in the type frame

lbl_type = ttk.Label(frm_btm_left, text='Type: ')
lbl_type.grid(row=2, column=0, padx= (10, 5), pady=(10, 5), sticky = E)

# Vallue for type
lbl_type_value = ttk.Label(frm_btm_left, text='Processing...')
lbl_type_value.grid(row=2, column=1, padx= (0, 10), pady=(10, 5), sticky = E)


#populate widgets in the info frame

#hp
lbl_hp = ttk.Label(frm_btm_right, text='HP : ')
lbl_hp.grid(row=0, column=0, sticky= E, padx= (10, 5), pady=(10, 5))
bar_hp = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum = 255)
bar_hp.grid(row =0, column = 1, padx= (0, 5), pady=(0, 5), sticky = W)


#attack 
lbl_attack = ttk.Label(frm_btm_right, text='Attack :  ')
lbl_attack.grid(row=1, column=0, sticky= E, padx= (10, 5), pady= 5)
bar_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum = 255)
bar_attack.grid(row =1, column = 1, padx= (0, 10), pady=5, sticky = W)

#defense
lbl_def = ttk.Label(frm_btm_right, text='Defense :  ')
lbl_def.grid(row=2, column=0, sticky= E)
bar_def = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum = 255)
bar_def.grid(row =2, column = 1, padx= (0, 10), pady=5, sticky = W)

#special attack
lbl_special_attack = ttk.Label(frm_btm_right, text='Special Attack :  ')
lbl_special_attack.grid(row=3, column=0, sticky= E, padx= (10, 5), pady= 5)
bar_special_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum = 255)
bar_special_attack.grid(row =3, column = 1, padx= (0, 10), pady=5, sticky = W)

#special defence
lbl_special_def = ttk.Label(frm_btm_right, text='Special Defense :  ')
lbl_special_def.grid(row=4, column=0, sticky= E, padx= (10, 5), pady= 5)
bar_special_def = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum = 255)
bar_special_def.grid(row =4, column = 1, padx= (0, 10), pady=5, sticky = W)

#speed
lbl_speed = ttk.Label(frm_btm_right, text='Speed :  ')
lbl_speed.grid(row=5, column=0, sticky= E, padx= (10, 5), pady=(10, 5))
bar_speed = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum = 255)
bar_speed.grid(row =5, column = 1, padx= (0, 5), pady=(0, 5), sticky = W)

# Loop until window is closed
root.mainloop()