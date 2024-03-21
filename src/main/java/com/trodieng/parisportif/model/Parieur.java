package com.trodieng.parisportif.model;

import javax.persistence.*;

import org.openxava.model.*;

import lombok.*;
@Entity @Getter @Setter
public class Parieur extends  Identifiable {
	@Column
	String name;
	@Column
	String email;
	@Column
	String motDePasse;
	@Column
	int jeton;

}
